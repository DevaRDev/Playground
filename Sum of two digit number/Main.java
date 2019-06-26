#include<stdio.h>
int main()
{
  int n=11,a,b,c;
  scanf("%d%d",&n);
  a=n%10;
  b=n/10;
  c=a+b;
  printf("%d",c);
  
  return 0;
}