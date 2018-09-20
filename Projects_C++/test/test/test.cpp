#include "test.h"

// static��Ա�趨���ſ���ʹ�� // Ӧ����cpp�ж��壬��Ϊmaintest.cpp��test.cpp�ж�������ͷ�ļ�test.h, maintest.cpp��ʹ�õ���test.cpp�е����ݣ� link��ʱ��maintest.cpp
// �ж�����nNum, ʹ�õ�test.cpp�ļ�ʱ����������test.hͷ�ļ����ֶ�����һ��nNum, ���Ի��ض������
int A::nNum = 0;	

void B::inner()
{
	cout << "This is out defined" << endl;
}

myString::myString()
{
	m_strData = NULL;
	m_nLen = 0;
}

myString::myString(const char *str)
{
	m_strData = new char[max_len+1];
	if (!m_strData)
	{
		// cerr���������͵���������ֱ���������Ļ��cout������������������ӻ������������Ļ
		cerr << "Allocation Error!\n";
		exit(1);
	}
	m_nLen = strlen(str);
	strcpy(m_strData, str);
}

char* myString::c_str() const
{
	return m_strData;
}

unsigned myString::length() const
{
	return m_nLen;
}

 myString operator+(const myString &obj1, const myString &obj2)
{
	 char *strTmp = new char[max_len + 1];
	 if (!strTmp)
	 {
		 cerr << "Allocation Error!\n";
		 exit(1);
	 }
	 strcpy(strTmp, obj1.m_strData);
	 strcat(strTmp, obj2.m_strData);
	 myString myStr(strTmp);

	 delete strTmp;
	return myStr;
}

 myString myString::operator+=(const myString &obj)
 {
	 char *tmp = m_strData;
	 m_strData = new char[max_len + 1];
	 if (!m_strData)
	 {
		 cerr << "Allocation Error!\n";
	 }
	 strcpy(m_strData, tmp);
	 strcat(m_strData, obj.m_strData);
	 myString strTmp(m_strData);

	 return strTmp;
 }

 bool myString::operator==(const myString &obj)
 {
	 if (strcmp(m_strData, obj.m_strData) == 0)
		 return true;
	 else
		 return false;
 }

 bool myString::operator!=(const myString &obj)
 {
	 if (strcmp(m_strData, obj.m_strData) != 0)
		 return true;
	 else
		 return false;
 }

 char myString::operator[](unsigned int nIdx)
 {
	 return m_strData[nIdx];
 }

 ostream &operator<<(ostream &os, myString &obj)
 {
	 os << obj.m_strData;
	 return os;
 }

 istream &operator>>(istream &is, myString &obj)
 {
	 is >> obj.m_strData;
	 return is;
 }

 myString &myString::subString(int nPos, int nLen)
 {
	 if (nPos <0 || nLen < 0 || nPos+ nLen -1 > max_len)
	 {
		 m_nLen = 0;
		 m_strData[0] = '\0';
	 }
	 else
	 {
		 if (nPos + nLen > m_nLen)
			 nLen = m_nLen - nPos;
		 m_nLen = nLen;

		 for (int i = 0,  j = nPos; i < nLen; i++, j++)
		 {
			 m_strData[i] = m_strData[j];
		 }
		 m_strData[nLen] = '\0';
	 }

	 return *this;
 }

 myWinsocket::myWinsocket(int nPort, const char* szIP, char cFlag)
 {
	 m_cFlag = cFlag;

	 // TCP �����
	 if (m_cFlag == '0')
	 {
		 WSADATA wsaDATA;
		 if (WSAStartup(MAKEWORD(2, 2), &wsaDATA) != 0)
		 {
			 cout << "�����׽���ʧ��:" << WSAGetLastError() << endl;
			 exception e("�����׽���ʧ��:" + WSAGetLastError());
			 throw e;
		 }

		 m_sockSrv = socket(AF_INET, SOCK_STREAM, 0);

		 SOCKADDR_IN addrSrv;
		 addrSrv.sin_family = AF_INET;
		 addrSrv.sin_port = htons(nPort);
		 addrSrv.sin_addr.S_un.S_addr = htonl(INADDR_ANY);

		 if (bind(m_sockSrv, (LPSOCKADDR)&addrSrv, sizeof(SOCKADDR_IN)) == SOCKET_ERROR)
		 {
			 cout << "���׽���ʧ��:" << WSAGetLastError() << endl;
			 exception e("���׽���ʧ��:" + WSAGetLastError());
			 throw e;
		 }

		 if (listen(m_sockSrv, 10) == SOCKET_ERROR)
		 {
			 cout << "�����׽���ʧ��:" << WSAGetLastError() << endl;
			 exception e("�����׽���ʧ��:" + WSAGetLastError());
			 throw e;
		 }

		 cout << "����������ɹ�����ʼ����" << endl;

		 // �ͻ�����Ϣ
		 SOCKADDR_IN addrClient;
		 int len = sizeof(SOCKADDR);
		 // acccept�������н�����ش���Ż�������, recv, cinҲ��������
		 m_sockConn = accept(m_sockSrv, (SOCKADDR*)&addrClient, &len);
		 if (m_sockConn == SOCKET_ERROR)
		 {
			 cout << "��������ʧ��:" << WSAGetLastError() << endl;
			 exception e("��������ʧ��:" + WSAGetLastError());
			 throw e;
		 }

		 cout << "�ɹ���ͻ��˽������ӣ��ͻ���IP:" << inet_ntoa(addrClient.sin_addr) << endl;
	 }
	 // TCP �ͻ���
	 else if (m_cFlag == '1')
	 {
		 WSADATA wsaDATA;
		 if (WSAStartup(MAKEWORD(2, 2), &wsaDATA) != 0)
		 {
			 cout << "�����׽���ʧ��:" << WSAGetLastError() << endl;
			 exception e("�����׽���ʧ��:" + WSAGetLastError());
			 throw e;
		 }

		 SOCKADDR_IN addrSrv;
		 addrSrv.sin_family = AF_INET;
		 addrSrv.sin_port = htons(nPort);
		 addrSrv.sin_addr.S_un.S_addr = inet_addr(szIP);

		 m_sockClient = socket(AF_INET, SOCK_STREAM, 0);
		 if(m_sockClient == SOCKET_ERROR)
		 {
			 cout << "�����׽���ʧ��:" << WSAGetLastError() << endl;
			 exception e("�����׽���ʧ��:" + WSAGetLastError());
			 throw e;
		 }

		 if (connect(m_sockClient, (struct sockaddr*)&addrSrv, sizeof(addrSrv)) == INVALID_SOCKET)
		 {
			 cout << "���ӷ�����ʧ��:" << WSAGetLastError() << endl;
			 exception e("���ӷ�����ʧ��:" + WSAGetLastError());
			 throw e;
		 }
	 }
	 // UDP �����
	 else if (m_cFlag == '2')
	 {
		 WSADATA wsaDATA;

		 if(WSAStartup(MAKEWORD(2, 2), &wsaDATA) != 0)
		 {
			 cout << "�����׽���ʧ��:" << WSAGetLastError() << endl;
			 char szError[128] = {0};
			 sprintf_s(szError, sizeof(szError) - 1, "�����׽���ʧ��:%d", WSAGetLastError());
			 exception e(szError);
			 throw e;
		 }

		 m_sockSrv = socket(AF_INET, SOCK_DGRAM, 0);
		 if (SOCKET_ERROR == m_sockSrv)
		 {
			 cout << "�����׽���ʧ��:" << WSAGetLastError() << endl;
			 char szError[128] = { 0 };
			 sprintf_s(szError, sizeof(szError) - 1, "�����׽���ʧ��:%d", WSAGetLastError());
			 exception e(szError);
			 throw e;
		 }

		 SOCKADDR_IN addrSrv;
		 addrSrv.sin_family = AF_INET;
		 addrSrv.sin_port = htons(nPort);
		 addrSrv.sin_addr.S_un.S_addr = htonl(INADDR_ANY);

		 if (bind(m_sockSrv, (LPSOCKADDR)&addrSrv, sizeof(SOCKADDR_IN)) == SOCKET_ERROR)
		 {
			 cout << "���׽���ʧ��:" << WSAGetLastError() << endl;
			 char szError[128] = { 0 };
			 sprintf_s(szError, sizeof(szError) - 1, "���׽���ʧ��:%d", WSAGetLastError());
			 exception e(szError);
			 throw e;
		 }

		 cout << "����������ɹ����ȴ��ͻ��˷�������" << endl;
	 }
	 // UDP �ͻ���
	 else
	 {
		 WSADATA wsaDATA;

		 if (WSAStartup(MAKEWORD(2, 2), &wsaDATA) != 0)
		 {
			 cout << "�����׽���ʧ��:" << WSAGetLastError() << endl;
			 char szError[128] = { 0 };
			 sprintf_s(szError, sizeof(szError) - 1, "�����׽���ʧ��:%d", WSAGetLastError());
			 exception e(szError);
			 throw e;
		 }

		 m_sockClient = socket(AF_INET, SOCK_DGRAM, 0);
		 if (SOCKET_ERROR == m_sockClient)
		 {
			 cout << "�����׽���ʧ��:" << WSAGetLastError() << endl;
			 char szError[128] = { 0 };
			 sprintf_s(szError, sizeof(szError) - 1, "�����׽���ʧ��:%d", WSAGetLastError());
			 exception e(szError);
			 throw e;
		 }

		 m_addrSrv.sin_family = AF_INET;
		 m_addrSrv.sin_port = htons(nPort);
		 m_addrSrv.sin_addr.S_un.S_addr = inet_addr(szIP);
	 }
 }

 int myWinsocket::sendMsg(const char *strSendmsg, int nSize)
 {
	 if (send(m_sockConn, strSendmsg, nSize, 0) == SOCKET_ERROR)
	 {
		 exception e("��������ʧ��" );
		 throw e;
	 }
 }

 int myWinsocket::revMsg(char *strRevmsg, int nSize)
 {
	 return recv(m_sockConn, strRevmsg, nSize, 0);
 }

 int myWinsocket::sendToSrv(const char *strSendmsg, int nSize)
 {
	 return send(m_sockClient, strSendmsg, nSize, 0);
 }

 int myWinsocket::revSrvMsg(char *strSendmsg, int nSize)
 {
	 return recv(m_sockClient, strSendmsg, nSize, 0);
 }

 int myWinsocket::recvMsgFrom(char *strSendmsg, int nSize)
 {
	 int nLen = sizeof(SOCKADDR);
	 return recvfrom(m_sockSrv, strSendmsg, nSize, 0, (SOCKADDR*)&m_addrClnt, &nLen);
 }

 int myWinsocket::sendMsgTo(const char *strSendmsg, int nSize)
 {
	 int nLen = sizeof(SOCKADDR);
	 return sendto(m_sockSrv, strSendmsg, nSize, 0, (SOCKADDR*)&m_addrClnt, nLen);
 }

 int myWinsocket::sendMsgToSrv(const char *strSendmsg, int nSize)
 {
	 int nLen = sizeof(SOCKADDR);
	 return sendto(m_sockClient, strSendmsg, nSize, 0, (SOCKADDR*)&m_addrSrv, nLen);
 }

 int myWinsocket::recvMsgFromSrv(char *strSendmsg, int nSize)
 {
	 int nLen = sizeof(SOCKADDR);
	 if (SOCKET_ERROR == recvfrom(m_sockClient, strSendmsg, nSize, 0, (SOCKADDR*)&m_addrSrv, &nLen))
	 {
		 cout << "��������ʧ��!" << endl;
		 return false;
	 }
	 return true;
 }

 myWinsocket::~myWinsocket()
 {
	 if (m_cFlag == '0')
	 {
		 closesocket(m_sockSrv);
		 closesocket(m_sockConn);
	 }
	 else if (m_cFlag == '1')
	 {
		 closesocket(m_sockClient);
	 }
	 else if (m_cFlag == '2')
	 {
		 closesocket(m_sockSrv);
	 }
	 else
	 {
		 closesocket(m_sockClient);
	 }

	 WSACleanup();
 }