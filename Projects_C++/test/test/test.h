//  WIN32_LEAN_AND_MEAN ����һЩ�����õ�API��windows.h���ܰ�����winsock.hͷ�ļ�������һЩAPI��accept�����ض���
#define WIN32_LEAN_AND_MEAN
#include<stdlib.h>
#include <stdio.h>
#include<iostream>
#include<fstream>
#include<string>
#include<iomanip>
#include<sstream>
#include "oracledb.h"
#include <windows.h>

#include<WinSock2.h>
#pragma comment(lib, "ws2_32.lib")

#include<pthread.h>
#pragma comment(lib, "pthreadVC2.lib")

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
	// ���ж�����
	static int nNum; 
	A()
	{
		m_iData = 1;
		m_pData = "hi";
		nNum++;
	}

	// �вι��캯��
	A(int a, char *b)
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

	// ����ͨ��ʵ���������
protected:
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

	// ���ж���ʵ�ֵĺ����ᱻ��������
	void print()
	{
		cout << m_nData << "," << m_nData << endl;
	}

	// ���const���򱨴�  // ����constֻ�ܱ���const��Ա��������
	void oper() /*const*/ 
	{
		m_nData = 1;
	}

	// static B obj();

	// ���ڲ�û�ж���ĺ������ᱻ��������
	void inner();	

	// ����׶��ڱ����õĵط����Ժ�����{}����������������Ҿ���ʹ��ʱ��������
	inline void inlinefunc()
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
		// enum�г�ԱĬ�ϴ�����0��ʼ��
		Monday = 1, 
		// ���µĳ�Աֵ�Ӵ˴���������һ��Ϊ4
		Tuesday = 3, 
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

	// �Զ��尲ȫ��������
	void mySprintf(char *szDst, unsigned int strlen, const char *szSrc)	
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

struct Object
{
	class E;
};

class Object::E
{
public:
	E(A *parent) : m_objA(parent)
	{}

	// ��������
	int operator() (char *tmp)	
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

// ��ģ��
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

// ���ⲿ������ģ��ĳ�Ա������������Ͷ���
template<class TYPE>	
TYPE F<TYPE>::Sub(TYPE a, TYPE b)
{
	return a*2 - b*2;
}

const int max_len = 1024;

// �Զ���string��
class myString
{
public:
	myString();
	myString(const char *str);

	myString operator+=(const myString &obj);

	// ����Ϊ��Ԫ������ʹ����Է�����myString��private,protected��Ա
	friend myString operator+(const myString &obj1, const myString &obj2);

	bool operator==(const myString &obj);
	bool operator!=(const myString &obj);
	char operator[](unsigned int nIdx);

	friend ostream &operator<<(ostream &os, myString &obj);
	friend istream &operator>>(istream &is, myString &obj);

	myString &subString(int nPos, int nIdx);

	// ����m_strData
	char* c_str() const;

	// ����m_nLen
	unsigned int length() const;

protected:

private:
	char *m_strData;
	unsigned int m_nLen;
};

class myWinsocket
{
public:
	myWinsocket() {};
	myWinsocket(int nPort, const char* szIP, char cFlag);
	~myWinsocket();

public:
	// TCP
	int sendMsg(const char *strSendmsg, int nSize);
	int revMsg(char *strRevmsg, int nSize);

	int sendToSrv(const char *strSendmsg, int nSize);
	int revSrvMsg(char *strSendmsg, int nSize);

	// UDP
	int recvMsgFrom(char *strSendmsg, int nSize);
	int sendMsgTo(const char *strSendmsg, int nSize);

	int sendMsgToSrv(const char *strSendmsg, int nSize);
	int recvMsgFromSrv(char *strSendmsg, int nSize);
protected:
private:
	char m_cFlag;

	SOCKET m_sockSrv;
	SOCKET m_sockClient;
	SOCKET m_sockConn;

	SOCKADDR_IN m_addrSrv;
	SOCKADDR_IN m_addrClnt;
};