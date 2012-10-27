#include<iostream>
#include<vector>
using namespace std;

#define THRESHOLD 2

//int **MATRIX_A, **MATRIX_B, **PRODUCT;
vector< vector<int> > MATRIX_A(1, vector<int>(1,0));
vector< vector<int> > MATRIX_B(1, vector<int>(1,0));
vector< vector<int> > PRODUCT(1, vector<int>(1,0));

/*---------- Function prototyping ---------- 
 *void strassen(vector< vector<int> > *, vector< vector<int> > *, vector< vector<int> > *, int);
 *void addMatrix(vector< vector<int> > *, vector< vector<int> > *, vector< vector<int> > *, int);
 *void subtractMatrix(vector< vector<int> > *, vector< vector<int> > *, vector< vector<int> > *, int);
 *void multiplyMatrix(vector< vector<int> > *, vector< vector<int> > *, vector< vector<int> > *, int);
 */

int main()
{
  /*---------- VARIABLES DECLARATION ---------- */
  int matrix_size, count = 0, i,j;

	  
  /*---------- INPUT ARRAY SIZE ---------- */
  std::cout<<"Input size of the square matrix (Mazimum is 32): ";
  std::cin>>matrix_size;

   /*---------- MEMORY ALLOCATION OF ARRAYS (vectors make it easy!!) ---------- */
  /*MATRIX_A = new int*[matrix_size];
  MATRIX_B = new int*[matrix_size];
  PRODUCT = new int*[matrix_size];

  for(i=0;i<matrix_size;i++) {
      MATRIX_A[i] = new int[matrix_size];
      MATRIX_B[i] = new int[matrix_size];
      PRODUCT[i] = new int[matriz_size];

      for(j=0;j<matrix_size;j++) {
	  MATRIX_A[i][j]=MATRIX_B[i][j]=PRODUCT[i][j]=count;
	}
	}
  */

  /*---------- Allocation of memory for Vector data members ---------- */
  for(int i=0;i<matrix_size;i++) {
    MATRIX_A.resize(matrix_size);
    MATRIX_B.resize(matrix_size);
    PRODUCT.resize(matrix_size);
    for(j=0;j<matrix_size;j++) {
      MATRIX_A[j].resize(matrix_size);
      MATRIX_B[j].resize(matrix_size);
      PRODUCT[j].resize(matrix_size);
    }
  }
  
  
  /*---------- INPUT MATRIX_A ---------- */
  std::cout<<"Enter the elements MATRIX A (row wise) "<<matrix_size<<" per row: "<<endl;
  for(i=0;i<matrix_size;i++) {
      std::cout<<"Enter elements for row "<<i+1<<":";
      for(j=0;j<matrix_size;j++) 
	std::cin>>MATRIX_A[i][j];
  }
  
  /*---------- INPUT MATRIX_B ---------- */
  std::cout<<"Enter the elements MATRIX B (row wise) "<<matrix_size<<" per row: "<<endl;
  for(i=0;i<matrix_size;i++) {
      std::cout<<"Enter elements for row "<<i+1<<":";
      for(j=0;j<matrix_size;j++) 
	std::cin>>MATRIX_B[i][j];
  }

  strassen(&MATRIX_A, &MATRIX_B, &PRODUCT, matrix_size);

  /*---------- OUTPUT OF RESULTS (RESULTANT MATRIX) ---------- */
  for(i=0;i<matrix_size;i++) {
    for(j=0;j<matrix_size;j++) 
      std::cout<<PRODUCT[i][j]<<"  ";
    cout<<endl;
  }
  

 return 0;
}



void strassen(vector< vector<int> > *a, vector< vector<int> > *b, vector< vector<int> > *result, int current_matrix_size)
{
  int next_matrix_size;
  vector< vector<int> > a1(current_matrix_size, vector<int>(current_matrix_size,0));
  vector< vector<int> > a2(current_matrix_size, vector<int>(current_matrix_size,0));
  vector< vector<int> > a3(current_matrix_size, vector<int>(current_matrix_size,0));
  vector< vector<int> > a4(current_matrix_size, vector<int>(current_matrix_size,0));
  vector< vector<int> > b1(current_matrix_size, vector<int>(current_matrix_size,0));
  vector< vector<int> > b2(current_matrix_size, vector<int>(current_matrix_size,0));
  vector< vector<int> > b3(current_matrix_size, vector<int>(current_matrix_size,0));
  vector< vector<int> > b4(current_matrix_size, vector<int>(current_matrix_size,0));
  vector< vector<int> > p1(current_matrix_size, vector<int>(current_matrix_size,0));
  vector< vector<int> > p2(current_matrix_size, vector<int>(current_matrix_size,0));
  vector< vector<int> > p3(current_matrix_size, vector<int>(current_matrix_size,0));
  vector< vector<int> > p4(current_matrix_size, vector<int>(current_matrix_size,0));
  vector< vector<int> > p5(current_matrix_size, vector<int>(current_matrix_size,0));
  vector< vector<int> > p6(current_matrix_size, vector<int>(current_matrix_size,0));
  vector< vector<int> > p7(current_matrix_size, vector<int>(current_matrix_size,0));
  vector< vector<int> > r(current_matrix_size, vector<int>(current_matrix_size,0));
  vector< vector<int> > s(current_matrix_size, vector<int>(current_matrix_size,0));
  vector< vector<int> > t(current_matrix_size, vector<int>(current_matrix_size,0));
  vector< vector<int> > u(current_matrix_size, vector<int>(current_matrix_size,0));
  vector< vector<int> > subtract_result(current_matrix_size, vector<int>(current_matrix_size,0));
  vector< vector<int> > add_result1(current_matrix_size, vector<int>(current_matrix_size,0));
  vector< vector<int> > add_result2(current_matrix_size, vector<int>(current_matrix_size,0));

  
  
  if(current_matrix_size<=THRESHOLD) {
    multiplyMatrix(a,b,result,current_matrix_size);
  }

  else {
    next_matrix_size = current_matrix_size/2;
    for (int ii=0;ii<next_matrix_size;ii++) {
      for (int jj=0;jj<next_matrix_size;jj++) {
	a1[ii][jj] = (a->at(ii)).at(jj);
	a2[ii][jj] = (a->at(ii)).at(jj+next_matrix_size);
	a3[ii][jj] = (a->at(ii+next_matrix_size)).at(jj);
	a4[ii][jj] = (a->at(ii+next_matrix_size)).at(jj+next_matrix_size);
	b1[ii][jj] = (b->at(ii)).at(jj);
	b2[ii][jj] = (b->at(ii)).at(jj+next_matrix_size);
	b3[ii][jj] = (b->at(ii+next_matrix_size)).at(jj);
	b4[ii][jj] = (b->at(ii+next_matrix_size)).at(jj+next_matrix_size);
      }
    }

    /* p1 calculation */
    subtractMatrix(&b2,&b4,&subtract_result,next_matrix_size);
    strassen(&a1,&subtract_result,&p1,next_matrix_size);

    /* p2 caculation */
    addMatrix(&a1,&a2,&add_result1,next_matrix_size);
    strassen(&add_result1,&b4,&p2,next_matrix_size);

    /* p3 calculation */
    addMatrix(&a3,&a4,&add_result1,next_matrix_size);
    strassen(&add_result1,&b1,&p3,next_matrix_size);

    /*p4 calculation */
    subtractMatrix(&b3,&b1,&subtract_result,next_matrix_size);
    strassen(&a4,&subtract_result,&p4,next_matrix_size);

    /* p5 calculation */
    addMatrix(&a1,&a4,&add_result1,next_matrix_size);
    addMatrix(&b1,&b4,&add_result2,next_matrix_size);
    strassen(&add_result1,&add_result2,&p5,next_matrix_size);

    /* p6 calculation */
    subtractMatrix(&a2,&a4,&subtract_result,next_matrix_size);
    addMatrix(&b3,&b4,&add_result1,next_matrix_size);
    strassen(&subtract_result,&add_result1,&p6,next_matrix_size);

    /* p7 calculation */
    subtractMatrix(&a1,&a3,&subtract_result,next_matrix_size);
    addMatrix(&b1,&b2,&add_result1,next_matrix_size);
    strassen(&subtract_result,&add_result1,&p7,next_matrix_size);

    /* r calculation */
    addMatrix(&p5,&p4,&add_result1,next_matrix_size);
    subtractMatrix(&add_result1,&p2,&subtract_result,next_matrix_size);
    addMatrix(&subtract_result,&p6,&r,next_matrix_size);

    /* s calculation */
    addMatrix(&p1,&p2,&s,next_matrix_size);

    /* t calulation */
    addMatrix(&p3,&p4,&t,next_matrix_size);

    /* u calculation */
    addMatrix(&p5,&p1,&add_result1,next_matrix_size);
    subtractMatrix(&add_result1,&p3,&subtract_result,next_matrix_size);
    subtractMatrix(&subtract_result,&p7,&u,next_matrix_size);

    for(int ii=0;ii<next_matrix_size;ii++) {
      for(int jj=0;jj<next_matrix_size;jj++) {
	(result->at(ii)).at(jj)=r[ii][jj];
	(result->at(ii)).at(jj+next_matrix_size)=s[ii][jj];
	(result->at(ii+next_matrix_size)).at(jj)=t[ii][jj];
	(result->at(ii+next_matrix_size)).at(jj+next_matrix_size)=u[ii][jj];
      }
    }
  }
}


void addMatrix(vector< vector<int> > *m1,vector< vector<int> > *m2,vector< vector<int> > *add_result, int matrix_size)
{
  for(int ii=0;ii<matrix_size;ii++) {
    for(int jj=0;jj<matrix_size;jj++) {
      (add_result->at(ii)).at(jj)=(m1->at(ii)).at(jj)+(m2->at(ii)).at(jj);
    }
  }
}

void subtractMatrix(vector< vector<int> > *m1,vector< vector<int> > *m2,vector< vector<int> > *subtract_result, int matrix_size)
{
  for(int ii=0;ii<matrix_size;ii++) {
    for(int jj=0;jj<matrix_size;jj++) {
      (subtract_result->at(ii)).at(jj)=(m1->at(ii)).at(jj)-(m2->at(ii)).at(jj);
    }
  }
}

void multiplyMatrix(vector< vector<int> > *m1,vector< vector<int> > *m2,vector< vector<int> > *multiply_result, int matrix_size)
{
  for(int ii=0;ii<matrix_size;ii++) {
    for(int jj=0;jj<matrix_size;jj++) {
      (multiply_result->at(ii)).at(jj)=0;
      for(int kk=0;kk<matrix_size;kk++) {
	(multiply_result->at(ii)).at(jj)+=(m1->at(ii)).at(kk)*(m2->at(kk)).at(jj);
      }
    }
  }
}
