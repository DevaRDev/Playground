#include<stdio.h>
int main()
{
 int n,x,y,z;
  scanf("%d",&n);

  x=n/100;
  y=n%10;
  z=x+y;
  printf("%d",z);
  return 0;
}