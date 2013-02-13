function [bins, range, whichBin] = binning(data, numberOfBins)
%BINNING Bins the values of a vector 
% Idea taken from
% http://stackoverflow.com/questions/419223/binning-in-matlab. Although,
% this returns `bins` which a probability distribution of the number of
% observations in `data` which lie in the same interval
% [Y,X,w] = BINNING(data, numberOfBins)
% data    - data vector
    min_val = min(data);
    topEdge = max(data) - min_val;
    range = topEdge;
    botEdge = 0;
    binEdges = linspace(botEdge, topEdge, numberOfBins);
    data = data - min_val;
    [bins, whichBin] = histc(data, binEdges);
    bins = (bins + 1)/(length(data) + numberOfBins); %Laplace Smoothing
end