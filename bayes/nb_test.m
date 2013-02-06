function [Ytest] = nb_test( Xtest, model, attributes)
%NB_TEST Naive Bayes tester for binary classification
    Ytest = zeros(length(Xtest),1);
    for i = 1:length(Xtest)
        class_1_prob = 1;
        class_2_prob = 1;
        d_count = 1;
        c_count = 1;
        for j = 1:length(attributes)
            if attributes(j) == 1 % discrete attribute
                % for class 1
                [~,~, whichbin] = binning([Xtest(i,j); model.range(d_count)], 10);
                class_1_prob = class_1_prob * model.bins(whichbin(1), d_count);
                % for class 2
                [~,~, whichbin] = binning([Xtest(i,j); model.range(d_count+1)], 10);
                class_2_prob = class_2_prob * model.bins(whichbin(1), d_count+1);
                d_count = d_count + 2;
            else                   % continuous attribute
                % for class 1
                class_1_prob = class_1_prob * normpdf(Xtest(i,j), model.mu(c_count), model.sigma(c_count));
                % for class 2
                class_2_prob = class_2_prob * normpdf(Xtest(i,j), model.mu(c_count+1), model.sigma(c_count+1));
                c_count = c_count + 2;
            end
        end
        if (class_1_prob > class_2_prob)
            Ytest(i) = 1;
        else
            Ytest(i) = 2;
        end
    end
end


