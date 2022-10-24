int noOfDominos(int m ,int n){
    int size;
    size = m * n;
    int dominos;
    // each domino takes a space of size 2
    dominos = size / 2;
    return dominos;
}