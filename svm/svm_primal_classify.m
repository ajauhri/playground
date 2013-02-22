function [ predictedY,w, b ] = svm_primal_classify( testX, trainX, trainY, C )
%SVM_PRIMAL_CLASSIFY
for i=1:length(trainX)
    for j=1:length(trainX)
        X(i,j) = 1/8*dot(trainX(i,:), trainX(j,:))^3;
    end
end
trainX = X;
testX = trainX;
[n, d] = size(trainX);

% change trainY with 0s to -1s
zero_indices = find(trainY < 1);
trainY(zero_indices) = -1;

% d is the number of weights for each feature in the training example 
% (d+1)th is b
% remaining variables are slack variables 
tot_dim = d + n + 1

% semi-positive matrix
H = zeros(tot_dim);
H(sub2ind([tot_dim, tot_dim], 1:d, 1:d)) = 1;

% linear coefficient vector
f = zeros(tot_dim, 1);
f(d+2:end) = C;

% add margin constraits
A = zeros(n, tot_dim);
A(1:n, 1:d) = bsxfun(@times, trainY, trainX);
A(1:n, d+1) = trainY;
A(sub2ind([n, tot_dim], 1:n, d+2:tot_dim)) = 1;

%add constraints for slack variables
A = [A; A];
A(n+1:n*2, 1:d+1)=0;

% quadprog accepts Ax <= b but our SVM uses Ax >= b
A = -A; 
b = -ones(n, 1);
b = [b;zeros(n,1)];

opts = optimset('Algorithm', 'interior-point-convex');
sol = quadprog(H, f, A, b, [], [], [], [], [], opts);

% sol has dimensions d+1+n i.e. tot_dim
w = sol(1:d);
b = sol(d+1);
%xi = sol(d+2:end);

% use w and b to get predictedY
predictedY = testX*w + b;

% margin is defined by w'x + b = 0, therefore (w'x + b) < 0 is for -1(or 0 in
% this case) and (w'x + b) > 0 is for +1
class_1 = predictedY < 0;
class_2 = predictedY > 0;

predictedY(class_1) = 0;
predictedY(class_2) = 1;
end

