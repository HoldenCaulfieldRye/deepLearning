bit.ly/1zQH73U

Geoff Hinton public lec MIT

current neural networks not good because don't work the way the brain does

they have too few levels of structure: only entities are neuron, layer, network. 

what's missing is notion of entity. this talk is abt building entity into the NN arch.

group some neurons within a layer into have activities of neurons in those subsets 
represent different properties of the same entity. the NN decides what the entities are 
and how they interact with each other, but there must be a built property that there's
going to be entities.

a mini-column is where one represents an entity.

a capsule will have 2 kinds of instantiation parameters:
prob that object present
generalised pose of the object

what capsules do that NNs dont is: take predictions from lower level capsules abt what
generalised pose should be, and look for preds that agree tightly. 
-> this is like "ran second half transforms" (??) in old school computer vision

a capsule has 



