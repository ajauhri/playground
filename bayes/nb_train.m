function [model] = nb_train( Xtrain, Ytrain, attributes)
%NB_TRAIN Naive Bayes for binary classification
%   Classification are represented as 'class 1' or 'class 2'.
%   Xtrain: Matrix/vector of observations for learning
%   Ytrain: Vector of observed labels/classification
%   attributes: vector of attribute indicators i.e. whether they are
%   discrete or continuous.

    class_1 = Ytrain==1; %data classified as 1
    class_2 = Ytrain==2; %data classified as 2
    
    mu = 'mu';  
    sigma = 'sigma';
    range = 'range';
    bins = 'bins';
   
    model = struct(mu, [], sigma, [], range, [], bins, []);
    
    for i = 1:length(attributes)
        if attributes(i) == 1 % discrete attribute
            % for class 1
            [bins, range] = (binning(Xtrain(class_1,i),10));
            model.bins = horzcat(model.bins, bins);
            model.range = [model.range; range];
            % for class 2
            [bins, range] = (binning(Xtrain(class_2,i), 10)); 
            model.bins = horzcat(model.bins, bins);
            model.range = [model.range; range];
            
        else                  % continuous attribute 
            % for class 1
            mu = mean(Xtrain(class_1, i));
            sigma = var(Xtrain(class_1, i));
            model.mu = [model.mu; mu];
            model.sigma = [model.sigma; sigma];
            % for class 2
            mu = mean(Xtrain(class_2, i));
            sigma = var(Xtrain(class_1, i));
            model.mu = [model.mu; mu];
            model.sigma = [model.sigma; sigma];    
        end
    end
end


