function [ predictedY, alpha, b ] = svm_dual_classify( testX, trainX, trainY, C, kernel )
%SVM_PRIMAL_CLASSIFY 
n = size(trainX, 1);

% change trainY with 0s to -1s
zero_indices = find(trainY < 1);
trainY(zero_indices) = -1;

% quadratic coefficient matrix
switch kernel
    case 'linear'
        K = trainX*trainX';
    case 'polynomial'
        K = ((trainX * trainX').^3)/8; 
    case 'RBF'      
        dist2 = repmat(sum((trainX.^2)', 1), [n 1])' + repmat(sum((trainX.^2)',1), [n 1]) - 2*trainX*(trainX');
        K = exp(-dist2/2);
end
size(trainY)
size(K)
H = (trainY*trainY') .* K; 

% linear coefficient vector
f = -ones(n, 1);

% equality constraint: sum_i alpha_i = 0
Aeq = trainY.';
beq = 0;

% bounds of variables
lb = zeros(n, 1);
ub = C * ones(n, 1);

% solve the problem
opts = optimset('Algorithm', 'interior-point-convex');
alpha = quadprog(H, f, [], [], Aeq, beq, lb, ub, [], opts);

% find the alpha that 0 < alpha < C
index = find(alpha > C/100 & alpha < 99*C/100);

% compute b
switch kernel
  case 'linear'
    su = 0;
    for j = 1:n
      su = su + alpha(j)*trainY(j)*(trainX(j,:)*trainX(index(1),:)');
    end   
    
  case 'polynomial'
    su = 0;
    for j = 1:n
      su = su + alpha(j)*trainY(j)*((trainX(j,:)*trainX(index(1),:)')^3)/8;
    end   
    
  case 'RBF'
    su = 0;
    for j = 1:n
      su = su + alpha(j)*trainY(j)*exp(-norm(trainX(j,:) - trainX(index(1),:),2)^2/2);
    end   
end

% compute w and b from alpha
% y(<w,x> + bb) = 1
w = trainX'*(alpha.*trainY);
b = 1/trainY(index(1)) - su;

predictedY = zeros(length(testX),1);
switch kernel
    case 'linear'
        for i=1:length(testX)
            su = 0;
            for j=1:length(trainX)
                su = su + alpha(j)*trainY(j)*dot(testX(i,:), trainX(j,:));
            end
            if su + b > 0
                predictedY(i) = 1;
            else
                predictedY(i) = 0;
            end
        end
    case 'polynomial'
        for i=1:length(testX)
            su = 0;
            for j=1:length(trainX)
                su = su + alpha(j) * trainY(j) * ((dot(testX(i,:), trainX(j,:))^3)/8);
            end
            if su + b > 0
                predictedY(i) = 1;
            else
                predictedY(i) = 0;
            end
        end
    case 'RBF'
        for i=1:length(testX)
            su = 0;
            for j=1:length(trainX)
                su = su + alpha(j) * trainY(j) * exp(-0.5*norm(testX(i,:) - trainX(j,:))^2);
            end
            if su + b > 0
                predictedY(i) = 1;
            else
                predictedY(i) = 0;
            end
        end
end
end

