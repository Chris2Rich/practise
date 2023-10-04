#include "patterns\graph.h"

int main(){
    Node A;
    Node B;
    Node C;
    Node D;
    Node E;

    Edge AB(&A,&B);
    Edge AC(&A,&B);
    Edge AD(&A,&D);
    Edge BD(&B,&D);
    Edge BE(&B,&E);
    Edge CE(&C,&E);
    Edge DE(&D,&E);

    A.EdgeArray.append(AB);
    B.EdgeArray.append(AB);
    A.EdgeArray.append(AC);
    C.EdgeArray.append(AC);
    A.EdgeArray.append(AD);
    D.EdgeArray.append(AD);
    B.EdgeArray.append(BD);
    D.EdgeArray.append(BD);
    B.EdgeArray.append(BE);
    E.EdgeArray.append(BE);
    C.EdgeArray.append(CE);
    E.EdgeArray.append(CE);
    D.EdgeArray.append(DE);
    E.EdgeArray.append(DE);
    return 0;
}