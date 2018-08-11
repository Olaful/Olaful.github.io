#include<stdlib.h>
#include<iostream>
#include<fstream>
#include<string>
#include<iomanip>
#include<sstream>
#include <windows.h>
#include "oracledb.h"

using   namespace   std;

#ifdef _WIN64
	#include "MyAPI.h"
	#pragma comment(lib, "MyAPI.lib")
#endif // _WIN64

#ifdef PI
#pragma message("PI ���Ѷ���")
#endif

#ifdef MAX
#pragma message("MAX ���Ѷ���")
#endif

class A
{
public:
	static int nNum; // ���ж�����
	A()
	{
		m_iData = 1;
		m_pData = "hi";
		nNum++;
	}

	A(int a, char *b) // �вι��캯��
	{
		m_iData = a;
		m_pData = b;
		nNum++;
	}

	virtual int add(double a, double b)
	{	
		if(strcmp(typeid(a).name(), "int") == 0 && strcmp(typeid(b).name(), "int") == 0)
		{
			return a + b;
		}
		else
		{
			cout << "��������ȷ������" << endl;
		}
	}

	float GetTriangleArea(float bottom, float height)
	{
		return bottom * height / 2;
	}

public:
	int m_iData;
	char *m_pData;

protected:	// ����ͨ��ʵ���������
	bool Check(double a, double b)
	{
		stringstream ss;
		ss << a;

		//while(a)
		//{
		//	a /= 10;
		//	iLen++;
		//}

		if(ss.str().length() >= 3)
		{
			cout << a << "���ȳ���3" << endl;
			return false;
		}

		ss.str("");
		ss << b;

		if(ss.str().length() > 4)
		{
			cout << b << "���ȳ���3" << endl;
			return false;
		}
		
		return true;
	}

	// virtual int sub() = 0;
};

class B : public A
{
public:
	B()
	{
		m_nData = 0;
		m_szData = NULL;
	};

	int add(double a, double b)
	{
		if (Check(a, b))
		{
			return a*2 + b*2;
		}
	}

	void print()	// ���ж���ʵ�ֵĺ����ᱻ��������
	{
		cout << m_nData << "," << m_nData << endl;
	}

	void oper() /*const*/  // ���const���򱨴�  // ����constֻ�ܱ���const��Ա��������
	{
		m_nData = 1;
	}

	// static B obj();

	void inner();	// ���ڲ�û�ж���ĺ������ᱻ��������

	inline void inlinefunc()	// ����׶��ڱ����õĵط����Ժ�����{}����������������Ҿ���ʹ��ʱ��������
	{
		cout << "This is a inline func" << endl;
	}

private:
	int m_nData;
	char *m_szData;
};

class C : public B
{
public:
	int add(int a, int b)
	{	
		if(strcmp(typeid(a).name(), "int") == 0 && strcmp(typeid(b).name(), "int") == 0)
		{
			return a*3 + b*3;
		}
		else
		{
			cout << "��������ȷ������" << endl;
		}
	}

	enum day
	{
		Monday = 1, // enum�г�ԱĬ�ϴ�����0��ʼ��
		Tuesday = 3, // ���µĳ�Աֵ�Ӵ˴���������һ��Ϊ4
		Wednesday,
		Thursday,
		Friday
	};

#define GetArea(r) 3.141576964357 * r * r;
		
};

class D
{
public:
	D() {};

	D(A *parent) : m_objA(parent)
	{}

	int add(int a, int b)
	{	
		if(strcmp(typeid(a).name(), "int") == 0 && strcmp(typeid(b).name(), "int") == 0)
		{
			return a*2 + b*2;
		}
		else
		{
			cout << "��������ȷ������" << endl;
		}
	}

	void Print()
	{
		cout << m_objA->m_iData << "," << m_objA->m_pData << endl;
	}

	void mySprintf(char *szDst, unsigned int strlen, const char *szSrc)	// �Զ��尲ȫ��������
	{
		if (szDst == NULL ||  szSrc == NULL)
		{
			return;
		}

		unsigned int len = 0;
		while (*szSrc != '\0' && len < strlen)
		{
			*szDst++ = *szSrc++;
			len++;
		}

		*szDst = '\0';
	}

private:
	A *m_objA;
};

int A::nNum;	// static��Ա�趨���ſ���ʹ��

struct Object
{
	class E;
};

class Object::E
{
public:
	E(A *parent) : m_objA(parent)
	{}

	int operator() (char *tmp)	// ��������
	{
		cout << tmp << endl;
	}

	int add(int a, int b)
	{	
		if(strcmp(typeid(a).name(), "int") == 0 && strcmp(typeid(b).name(), "int") == 0)
		{
			return a*2 + b*2;
		}
		else
		{
			cout << "��������ȷ������" << endl;
		}
	}

	void Print()
	{
		cout << m_objA->m_iData << "," << m_objA->m_pData << "," << m_objA->nNum << "," << endl;
	}

private:
	A *m_objA;
};

template<class TYPE>
class F
{
public:
	TYPE add(TYPE a, TYPE b)
	{	
		return a*2 + b*2;
	}

	TYPE Sub(TYPE a, TYPE b);
private:
};

template<class TYPE>	// ���ⲿ������ģ��ĳ�Ա������������Ͷ���
TYPE F<TYPE>::Sub(TYPE a, TYPE b)
{
	return a*2 - b*2;
}

void B::inner()
{
	cout << "This is out defined" << endl;
}