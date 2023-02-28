#include <iostream>

using namespace std;

int main(int argc, char** argv) {

  int a,b,c,d;

  std::cin >> a >> b >> c >> d;

  int diferenca = (a*b-c*d);
  
  std::cout <<"DIFERENCA = "<<diferenca<<'\n';
  return 0;
}