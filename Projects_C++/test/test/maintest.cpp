#include"test.h"

	template <typename T>
	inline T const& Max (T const& a, T const& b) 
	{ 
    return a < b ? b:a; 
	}

	void *pthdsendMsg(void *args)
	{
		try
		{
			myWinsocket objmyWinsocket;

			objmyWinsocket = *((myWinsocket*)args);

			int nRevbufsize = 1024;

			string strSend;

			while (true)
			{
				strSend = "";
				// �������״̬
				cin.clear();
				// ������뻺����
				cin.sync();

				cout << "���͵���Ϣ:";
				// cin�����к��пո�Ļ������Կո�Ϊ�ָ�������������ݷֶΣ���һ��cin��ʱ����Զ���δ�͵��������ķֶ���Ϣ���뵽������
				//cin >> szSendbuf;
				getline(cin, strSend);
				objmyWinsocket.sendMsg(strSend.c_str(), nRevbufsize);
			}
		}
		catch (const std::exception& e)
		{
			cout << "������Ϣ:" << e.what() << endl;
		}

		return NULL;
	}

	void *pthdRecvMsg(void *args)
	{
		try
		{
			myWinsocket objmyWinsocket;

			objmyWinsocket = *((myWinsocket*)args);

			char szRevbuf[1024];
			szRevbuf[0] = '\0';
			int nRevbufsize = sizeof(szRevbuf);

			while (true)
			{
				cout << "�ͻ�����Ϣ:";
				objmyWinsocket.revMsg(szRevbuf, nRevbufsize);
				cout << szRevbuf << endl;
				szRevbuf[0] = '\0';
			}
		}
		catch (const std::exception& e)
		{
			cout << "������Ϣ:" << e.what() << endl;
		}

		return NULL;
	}

//void main()	// main����return�Ļ����������Զ���Ŀ���ļ��м���return 0����������ڱ���ʱ��ʹ��int main(int argc, char *argv[])
int main(int argc, char *argv[])
{
	cout << "welcome" << endl;
	cout << "��������:" << argc << endl;

	for (size_t i = 0; i < argc; i++)
	{
		cout << "����ֵ��" << argv[i] << endl;
	}

	SYSTEMTIME st;
	::GetLocalTime(&st);
	char szTime[32];
	sprintf_s(szTime, "systemtime: %d/%d/%d %d:%d:%d\n", st.wYear, st.wMonth, st.wDay, st.wHour, st.wMinute, st.wSecond);
	cout << szTime << endl;

	char cSwitch = 'a';

	if (cSwitch == 'a')
	{
			int i = 39;
			int j = 20;
			cout << "Max(i, j): " << Max(i, j) << endl;

			int p4[5] = {1, 2, 3, 4, 5};
			char *p = "ppppp";
			char c = 0xff;
			// ����ascii��ʮ�����Ƶ�a��ӦLF(���м�) ������ʾ�ַ�
			unsigned char cc = 0xa;
			// 7 ->BEL(����)
			char ccc = 0x7;
			// 21->! ����ʾ�ַ�
			char cccc = 0x21;
			// '\0'��β���������Ϊ4���ַ�
			char p1[5] = "Dddd"; 
			char p2[5] = "dddd";
			char sz[] = "abcdf";
			char *szPtr[] = {"you", "me", "him"};
			unsigned int a = 1;
			int b = 10;
			// 0xffת����ʮ����255
			int a2 = 0xff;
		
			cout << "get cc:" << cc << endl;
			cout << "get ccc:" << ccc << endl;
			cout << "get cccc:" << cccc << endl;
			cout << "get c:" << c << endl;
			cout << "get a:" << a2 << endl;
			// -2�Ĳ���1.....10, ����intת����unsigned int ����λ1��������ֵλ
			cout << "a*(-2):" << a * (-2) << endl;
			// λ����� b*2^1
			cout << "b << 1:" <<  (b<<1 )<< endl;	
			cout << "b >> 1:" << (b >> 1) << endl;
			cout << szPtr[0] << endl;
			// ָ�����ָ����׵�ַ��ʼ��ȡ����
			cout << "get p content:" << p << endl; 
			cout << "get p adress :" << &p << endl;
			cout << "get *p:" << *p << endl;
			cout << "get p+1 adress :" << &p+1 << endl;
			cout << "get p+2 adress :" << &p+2 << endl;
			cout << "get p head+1 :" << p+1 << endl;
			cout << "get p head-1 :" << p-1 << endl;
			cout << "get sizeof(p4) :" << sizeof(p4) << endl;
			cout << "get sizeof(*p4) :" << sizeof(*p4) << endl;
			// ��ȡָ������ĳ���
			cout << "get sizeof(*p) :" << sizeof(*p) << endl; 
			// ��ȡռ�õ��ڴ泤�� 32λ�������½����4��64λ��8
			cout << "get sizeof(p) :" << sizeof(p) << endl; 
			// ��ȡ���ݳ���
			cout << "get strlen(p) :" << strlen(p) << endl; 
			cout << "get sizeof(p1) :" << sizeof(p1) << endl;
			cout << "get strlen(p1) :" << strlen(p1) << endl;
			cout << "get sizeof(sz) :" << sizeof(sz) << endl;

			cout << "get p1+1:" << p1+1 << endl;
			cout << "get p1-1:" << p1 - 1 << endl;
			cout << "get p1[4]:" << p1[4] << endl;
			cout << "get *p1+1:" << *p1+1 << endl;
			cout << "get *p2+1:" << *p2+1 << endl;
			cout << "get type p4:" << typeid(p4).name() << endl;

			// 'a' asciiת����ʮ����97���1
			cout << "get ascii++:" << 'a'+1 << endl; 
			// �൱��ָ�������ƶ�һλ
			cout << "get str++:" << "dddd"+1 << endl; 

			char *p3 = p1;
			cout << "get p3:" << p3 << endl; 
	}
	
	if (cSwitch == 'b')
	{
		A *objA;

		B objB;
		// ָ���ַ��ֵ����ʵ���麯����̬
		objA = &objB;	
		int sum = objA->add(1234, 2);
		cout << "a+b:" << sum << endl;

		float fArea = objB.GetTriangleArea(1.0, 3.0);
		cout << "triarea:" << fixed << setprecision(2) << fArea << endl;

		//A objA1;
		//B objB1();
		//objA1 = objB1;
		//int sum1 = objA1.add(1, 2);
		//cout << "a+b:" << sum1 << endl;

		//C objC;
		//A *objA2 = &objC;
		//cout << "a+b:" << objA2->add(1, 2) << endl;

		//B objB2;
		//D objD(&objB2);
		//objD.Print();

		// �����вι��캯��
		A objA2(5, "hello");
		Object::E objE(&objA2);
		objE.Print();

		// ����ģ��Fʵ����ΪF��, ��β���<��������>���޷�ʵ����F��
		F<int> objF;	
		cout << objF.add(2,3) << endl;

		// ����ģ��Fʵ����ΪF��
		F<float> objF1;	
		cout << objF1.add(2.1f,3.1f) << endl;

		F<float> objF2;
		cout << objF2.Sub(2.1,3.1) << endl;

		B objB1;
		objB1.inlinefunc();
		objB1.inner();

		cout << C::Monday << endl;
		cout << C::Tuesday << endl;
		cout << C::Wednesday << endl;

		D objD;
		char szDst[3];
		char *szSrc = "source";

		objD.mySprintf(szDst, sizeof(szDst) - 1, szSrc);
		cout << "mySprintf:" << szDst << endl;
	}

	if (cSwitch == 'c')
	{
		ifstream sourcefile("E:\\C++\\myfile\\1.txt");
		ofstream destfile("E:\\C++\\myfile\\2.txt", ofstream::app);

		string temp;
		if (!sourcefile.is_open())
		{
			cout << "�ļ�E:\\C++\\myfile\\1.txt���ܳɹ���" << endl; 
		}

		while (getline(sourcefile, temp))
		{
			destfile << temp;
		}
	}

	// ʹ���ⲿdll
	if (cSwitch == 'd')
	{
#ifdef _WIN64
		cout << "Sub:" << Sub(10, 5) << endl;
#endif // _WIN64
		//cout << "Add:" << Add(10, 5) << endl;
	}

	if (cSwitch == 'e')
	{
		float fData = GetArea(2);
		cout << "data:" << fData << endl;
	}

	if(cSwitch == 'f')
	{
		// fstream �̳���iostream, iostream ͬʱ�̳���istream��ostream�� ifstream�̳���istream��ofstream�̳���ostream
		ifstream sourcefile1("E:\\C++\\myfile\\1.txt");
		ifstream sourcefile2("E:\\C++\\myfile\\2.txt");
		// �������ʽ��(�ڴ浽�ļ�) �򿪲�����ļ�
		ofstream destfile("E:\\C++\\myfile\\3.txt", ios::out|ios::trunc); 
	
		string temp1;
		string temp2;
		string temp3 = "";

		if (!sourcefile1.is_open())
		{
			cout << "�ļ�E:\\C++\\myfile\\1.txt���ܳɹ���" << endl; 
		}
		if (!sourcefile2.is_open())
		{
			cout << "�ļ�E:\\C++\\myfile\\2.txt���ܳɹ���" << endl; 
		}
		
		while (getline(sourcefile1, temp1))
		{
			while(getline(sourcefile2, temp2))
			{
				// strcmp ����ֵ  ����1>����2 1  ����1<����2 -1 ����1=����2 0
				if(strcmp(temp1.c_str(), temp2.c_str()) == 0) 
				{
					temp3 = "";
					break;
				}
				else
				{
					temp3 = temp1;
				}
			}

			if (!temp3.empty())
				destfile << temp3 + "\n";

			// �������־λ����λ����ͷ
			sourcefile2.clear();
			sourcefile2.seekg(0);
		}

		sourcefile1.close();
		sourcefile2.close();
	}

	if (cSwitch == 'g')
	{
		DBOper dbOper;
   
		bool bConn=dbOper.ConnToDB("Provider=OraOLEDB.Oracle;Persist Security Info=True;DataSource=ORCLss","tbq","tbq");
		if (false == bConn)
		{
		    printf("�������ݿ���ִ���\n");
		}
		else
		{
			printf("�������ݿ�ɹ�!\n");

			_RecordsetPtr pRst;

			char cAtion = 'Q';
			char sql[255] = { 0 };
 
			if (cAtion == 'Q') 
			{
				strcpy_s(sql, "select* from test");
				//pRst = dbOper.ExecuteSql(sql);

				if (NULL == pRst)
				{
				    printf("��ѯ���ݳ��ִ���\n");
				}
				else if(pRst->adoEOF)
				{
				    pRst->Close();
				    printf("Thereis no records in this table\n");
				}
				else
				{
					printf("���ڲ�ѯ...\n");
					printf("ID\tNAME\n");
					_variant_t vSno, vName;
					while(!pRst->adoEOF)
					{
					    //pRst->MoveFirst();//��¼��ָ���ƶ�����ѯ�������ǰ��
						// 0��ʾ��һ���ֶ�
					    vSno = pRst->GetCollect(_variant_t((long)0)); 
					    vName = pRst->GetCollect(_variant_t("name"));
 
					    printf("%s\t%s\n",(LPSTR)(LPCSTR)(_bstr_t)vSno, (LPSTR)(LPCSTR)_bstr_t(vName));
					    pRst->MoveNext();
					}
				}
			}
			else if (cAtion == 'A')
			{
				// ��ʼ����
				dbOper.TransBegin(); 
				strcpy_s(sql, "insert into test(ID, NAME) values(7, '���')");
				//pRst = dbOper.ExecuteSql(sql);

				_RecordsetPtr pRst1;
				//pRst1 = dbOper.ExecuteSql("insert into test(ID, NAME) values(7, '���')");

				if (NULL !=pRst && NULL != pRst1)
				{
					printf("�������ݳɹ�\n");
				}
				else
				{
					// �ع�����
					dbOper.RollbakTrans(); 
				}
				// ���δ�ύ�����ύ
				dbOper.CheckCommit(); 
			}
			else if (cAtion == 'D')
			{
				sprintf_s(sql, "deletefrom test where id = '%d'",1);
				//pRst = dbOper.ExecuteSql(sql);
				if (NULL !=pRst)
				{
					printf("ɾ�����ݳɹ�\n");
				}
			}
		}
	}

	if (cSwitch == 'h')
	{
		DBOper dbOper("tbq","tbq");

		string sql = "select * from test";

		int nID = 0;
		char szName[16] = "";

		dbOper.Open(sql);
		dbOper.Execute();
		cout << "id" << "\t" << "name" << endl;
		while(!dbOper.Eof())
		{
			dbOper.GetValue("id", nID);
			dbOper.GetValue("name", szName);
			cout << nID << "\t";
			cout << szName << endl;
			dbOper.MoveNext();
		}

		dbOper.Close();

		dbOper.Open(sql);
	}

	if (cSwitch == 'i')
	{
		char *strTest = new char[1];
		int i = 0;
		while (*strTest++)
		{
			i++;
		}
		//strTest = new char[1];
		cout << "size:" << i<< endl;
		// ʹ�õ�����ʽת���� �൱��myString str("hello");
		myString str = "hello"; 
		cout << "myString output:" << str.c_str() << endl;
	}

	if (cSwitch == 'j')
	{
		WSADATA wsaData;
		int port = 5099;
		char buf[] = "������: ��ӭ��¼......\n";

		// �����׽���
		if (WSAStartup(MAKEWORD(2, 2), &wsaData) != 0)
		{
			printf("�����׽���ʧ�ܣ�%d......\n", WSAGetLastError());
			return 1;
		}

		// socket()
		SOCKET sockSrv = socket(AF_INET, SOCK_STREAM, 0);

		// ��ʼ��IP�Ͷ˿���Ϣ
		SOCKADDR_IN addrSrv;
		addrSrv.sin_family = AF_INET;
		addrSrv.sin_port = htons(port); // 1024���ϵĶ˿ں�
		addrSrv.sin_addr.S_un.S_addr = htonl(INADDR_ANY);

		// bind()
		if (bind(sockSrv, (LPSOCKADDR)&addrSrv, sizeof(SOCKADDR_IN)) == SOCKET_ERROR)
		{
			printf("�׽��ְ�ʧ�ܣ�%d......\n", WSAGetLastError());
			return 1;
		}

		// listen()
		if (listen(sockSrv, 10) == SOCKET_ERROR) {
			printf("�׽��ּ���ʧ�ܣ�%d......\n", WSAGetLastError());
			return 1;
		}

		// �ͻ�����Ϣ
		SOCKADDR_IN addrClient;
		int len = sizeof(SOCKADDR);

		// ��ʼ����
		printf("����������ɹ�......��ʼ����...\n");
		while (1)
		{
			// �ȴ��ͻ�������  
			// acccept�������н�����ش���Ż�������, cinҲ��������
			SOCKET sockConn = accept(sockSrv, (SOCKADDR *)&addrClient, &len);
			if (sockConn == SOCKET_ERROR) {
				printf("��������ʧ�ܣ�%d......\n", WSAGetLastError());
				break;
			}

			printf("��ͻ��˽�������......IP��[%s]\n", inet_ntoa(addrClient.sin_addr));

			// ��������
			if (send(sockConn, buf, sizeof(buf), 0) == SOCKET_ERROR) {
				printf("��������ʧ��......\n");
				break;
			}

			char recvBuf[100];
			memset(recvBuf, 0, sizeof(recvBuf));
			// ��������
			recv(sockConn, recvBuf, sizeof(recvBuf), 0);
			printf("�յ����ݣ�%s\n", recvBuf);

			closesocket(sockConn);
		}

		// �ر��׽���
		closesocket(sockSrv);
		WSACleanup();
		system("pause");

		return 0;
	}

	if (cSwitch == 'k')
	{
		WSADATA wsaData;
		int port = 5099;
		char buff[1024];
		memset(buff, 0, sizeof(buff));

		// �����׽���
		if (WSAStartup(MAKEWORD(2, 2), &wsaData) != 0)
		{
			printf("�����׽���ʧ�ܣ�%d......\n", WSAGetLastError());
			return 1;
		}

		// ��ʼ��IP�Ͷ˿���Ϣ
		SOCKADDR_IN addrSrv;
		addrSrv.sin_family = AF_INET;
		addrSrv.sin_port = htons(port);
		addrSrv.sin_addr.S_un.S_addr = inet_addr("127.0.0.1");

		// socket()
		SOCKET sockClient = socket(AF_INET, SOCK_STREAM, 0);
		if (SOCKET_ERROR == sockClient) {
			printf("�����׽���ʧ�ܣ�%d......\n", WSAGetLastError());
			return 1;
		}

		// �������������������
		if (connect(sockClient, (struct  sockaddr*)&addrSrv, sizeof(addrSrv)) == INVALID_SOCKET)
		{
			printf("���ӷ�����ʧ�ܣ�%d......\n", WSAGetLastError());
			return 1;
		}
		else
		{
			// ��������
			recv(sockClient, buff, sizeof(buff), 0);
			printf("�յ����ݣ�%s\n", buff);

			// ��������
			char buf[] = "�ͻ��ˣ������¼......";
			send(sockClient, buf, sizeof(buf), 0);
		}

		// �ر��׽���
		closesocket(sockClient);
		WSACleanup();

		return 0;
	}

	if(cSwitch == 'l')
	{
		try
		{
			int nPort = 5099;
			char *szIP = "";
			myWinsocket objmyWinsocket(nPort, szIP, '0');

			char szRevbuf[1024];
			szRevbuf[0] = '\0';
			int nRevbufsize = sizeof(szRevbuf);

			string strSend;

			while (true)
			{
				cout << "�ͻ�����Ϣ:";
				objmyWinsocket.revMsg(szRevbuf, nRevbufsize);
				cout << szRevbuf << endl;
				szRevbuf[0] = '\0';

				strSend = "";
				// �������״̬
				cin.clear();
				// ������뻺����
				cin.sync();

				cout << "���͵���Ϣ:";
				// cin�����к��пո�Ļ������Կո�Ϊ�ָ�������������ݷֶΣ���һ��cin��ʱ����Զ���δ�͵��������ķֶ���Ϣ���뵽������
				//cin >> szSendbuf;
				getline(cin, strSend);
				objmyWinsocket.sendMsg(strSend.c_str(), nRevbufsize);
			}
		}
		catch(const std::exception& e)
		{
			cout << "������Ϣ:" << e.what() << endl;
		}
	}

	if (cSwitch == 'm')
	{
		try
		{
			int nPort = 5099;
			char *szIP = (argv[1] != NULL ? argv[1] :  "127.0.0.1");
			myWinsocket objmyWinsocket(nPort, szIP, '1');

			char szRevbuf[1024];
			szRevbuf[0] = '\0';
			int nRevbufsize = sizeof(szRevbuf);

			string strSend;

			while (true)
			{
				strSend = "";
				cout << "���͵���Ϣ:";
				getline(cin, strSend);
				objmyWinsocket.sendToSrv(strSend.c_str(), nRevbufsize);

				cout << "�������Ϣ:";
				objmyWinsocket.revSrvMsg(szRevbuf, nRevbufsize);
				cout << szRevbuf << endl;
				szRevbuf[0] = '\0';
			}
		}
		catch (const std::exception& e)
		{
			cout << "������Ϣ:" << e.what() << endl;
		}
	}

	if (cSwitch == 'n')
	{
		try
		{
			int nPort = 5099;
			char *szIP = "";
			myWinsocket objmyWinsocket(nPort, szIP, '2');

			char szRevbuf[1024];
			szRevbuf[0] = '\0';
			int nRevbufsize = sizeof(szRevbuf);

			string strSend;

			while (true)
			{
				cout << "�ͻ�����Ϣ:";
				objmyWinsocket.recvMsgFrom(szRevbuf, nRevbufsize);
				cout << szRevbuf << endl;
				szRevbuf[0] = '\0';

				strSend = "";
				// �������״̬
				cin.clear();
				// ������뻺����
				cin.sync();

				cout << "���͵���Ϣ:";
				// cin�����к��пո�Ļ������Կո�Ϊ�ָ�������������ݷֶΣ���һ��cin��ʱ����Զ���δ�͵��������ķֶ���Ϣ���뵽������
				//cin >> szSendbuf;
				getline(cin, strSend);
				objmyWinsocket.sendMsgTo(strSend.c_str(), nRevbufsize);
			}
		}
		catch (const std::exception& e)
		{
			cout << "������Ϣ:" << e.what() << endl;
		}
	}

	if (cSwitch == 'o')
	{
		try
		{
			int nPort = 5099;
			char *szIP = (argv[1] != NULL ? argv[1] : "127.0.0.1");
			myWinsocket objmyWinsocket(nPort, szIP, '3');

			char szRevbuf[1024];
			szRevbuf[0] = '\0';
			int nRevbufsize = sizeof(szRevbuf);

			string strSend;

			while (true)
			{
				strSend = "";
				cout << "���͵���Ϣ:";
				getline(cin, strSend);
				objmyWinsocket.sendMsgToSrv(strSend.c_str(), nRevbufsize);

				cout << "�������Ϣ:";
				objmyWinsocket.recvMsgFromSrv(szRevbuf, nRevbufsize);
				cout << szRevbuf << endl;
				szRevbuf[0] = '\0';
			}
		}
		catch (const std::exception& e)
		{
			cout << "������Ϣ:" << e.what() << endl;
		}
	}

	if (cSwitch == 'p')
	{
		//pthread_t pthsend, pthrecv;

		//try
		//{
		//	int nPort = 5099;
		//	char *szIP = "";
		//	myWinsocket objmyWinsocket(nPort, szIP, '0');

		//// �Ѻ��������߳��� �����������Ϣ������һ���߳�
		//pthread_create(&pthrecv, NULL, pthdRecvMsg, (void*)&objmyWinsocket);
		//pthread_create(&pthsend, NULL, pthdsendMsg, (void*)&objmyWinsocket);

		//// Pthread�����̺߳����ʹ��join��detach�ͷ��߳���Դ
		//pthread_join(pthrecv, NULL);
		//pthread_join(pthsend, NULL);
		//}
		//catch (const std::exception& e)
		//{
		//	cout << "������Ϣ:" << e.what() << endl;
		//}

		return true;
	}

	if (cSwitch == 'q')
	{
		int sz[] = { 8, 9, 8, 1, 4, 7, 6, 5, 3, 2, 10 };
		int nLen = sizeof(sz) / sizeof(sz[0]);
		int temp;
		for (size_t i = 0; i < nLen; i++)
		{
			for (size_t j = 0; j < nLen - i - 1; j++)
			{
				if (sz[j] > sz[j+1])
				{
					temp = sz[j + 1];
					sz[j + 1] = sz[j];
					sz[j] = temp;
				}
			}
		}
		for (size_t i = 0; i < nLen; i++)
		{
			cout << sz[i] << ",";
		}
	}

	system("pause");
}