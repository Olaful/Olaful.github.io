#include "MyAPI.h"

#include<iostream>
#include<string>

using   namespace   std;

int Sub(int a, int b)
{
	if(strcmp(typeid(a).name(), "int") == 0 && strcmp(typeid(b).name(), "int") == 0)
	{
		return a - b;
	}
	else
	{
		cout << "��������ȷ������" << endl;
		return 0;
	}
}

int Adda(int a, int b)
{
	if(strcmp(typeid(a).name(), "int") == 0 && strcmp(typeid(b).name(), "int") == 0)
	{
		return a + b;
	}
	else
	{
		cout << "��������ȷ������" << endl;
		return 0;
	}
}