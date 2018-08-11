#include"test.h"


	template <typename T>
	inline T const& Max (T const& a, T const& b) 
	{ 
    return a < b ? b:a; 
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

	char cSwitch = 'b';

	if (cSwitch == 'a')
	{
			int i = 39;
			int j = 20;
			cout << "Max(i, j): " << Max(i, j) << endl;

			int p4[5] = {1, 2, 3, 4, 5};
			char *p = "pppp";
			char p1[5] = "Dddd"; // '\0'��β���������Ϊ4���ַ�
			char p2[5] = "dddd";
			char sz[] = "abcdf";
			char *szPtr[] = {"you", "me", "him"};
			unsigned int a = 1;
			int b = 10;

			cout << "a*(-2):" << a * (-2) << endl;	// -2�Ĳ���1.....10, ����intת����unsigned int ����λ1��������ֵλ
			cout << "b << 1:" <<  (b<<1 )<< endl;	// λ����� b*2^1
			cout << "b >> 1:" << (b >> 1) << endl;
			cout << szPtr[0] << endl;
			cout << "get p content:" << p << endl; // ָ�����ָ����׵�ַ��ʼ��ȡ����
			cout << "get p adress :" << &p << endl;
			cout << "get *p:" << *p << endl;
			cout << "get p+1 adress :" << &p+1 << endl;
			cout << "get p+2 adress :" << &p+2 << endl;
			cout << "get p head+1 :" << p+1 << endl;
			cout << "get p head-1 :" << p-1 << endl;
			cout << "get sizeof(p4) :" << sizeof(p4) << endl;
			cout << "get sizeof(*p4) :" << sizeof(*p4) << endl;
			cout << "get sizeof(*p) :" << sizeof(*p) << endl; // ��ȡָ������ĳ���
			cout << "get sizeof(p) :" << sizeof(p) << endl; // ��ȡռ�õ��ڴ泤�� 32λ�������½����4��64λ��8
			cout << "get strlen(p) :" << strlen(p) << endl; // ��ȡ���ݳ���
			cout << "get sizeof(p1) :" << sizeof(p1) << endl;
			cout << "get strlen(p1) :" << strlen(p1) << endl;
			cout << "get sizeof(sz) :" << sizeof(sz) << endl;

			cout << "get p1+1:" << p1+1 << endl;
			cout << "get p1-1:" << p1 - 1 << endl;
			cout << "get p1[4]:" << p1[4] << endl;
			cout << "get *p1+1:" << *p1+1 << endl;
			cout << "get p2:" << *p2+1 << endl;
			cout << "get type p4:" << typeid(p4).name() << endl;

			cout << "get ascii++:" << 'a'+1 << endl;   // 'a' asciiת����ʮ����97���1
			cout << "get str++:" << "dddd"+1 << endl; // �൱��ָ�������ƶ�һλ

			char *p3 = p1;
			cout << "get p3:" << p3 << endl; 
	}
	
	if (cSwitch == 'b')
	{
		A *objA;

		B objB;
		objA = &objB;	// ָ���ַ��ֵ����ʵ���麯����̬
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

		A objA2(5, "hello");	// �����вι��캯��
		Object::E objE(&objA2);
		objE.Print();

		F<int> objF;	// ����ģ��Fʵ����ΪF��, ��β���<��������>���޷�ʵ����F��
		cout << objF.add(2,3) << endl;

		F<float> objF1;	// ����ģ��Fʵ����ΪF��
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
		ofstream destfile("E:\\C++\\myfile\\3.txt", ios::out|ios::trunc); // �������ʽ��(�ڴ浽�ļ�) �򿪲�����ļ�
	
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
				if(strcmp(temp1.c_str(), temp2.c_str()) == 0) // strcmp ����ֵ  ����1>����2 1  ����1<����2 -1 ����1=����2 0
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
 
			if (cAtion == 'Q') // ��ѯ����
			{
				strcpy_s(sql, "select* from test");
				pRst = dbOper.ExecuteSql(sql);

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
					    vSno = pRst->GetCollect(_variant_t((long)0)); // 0��ʾ��һ���ֶ�
					    vName = pRst->GetCollect(_variant_t("name"));
 
					    printf("%s\t%s\n",(LPSTR)(LPCSTR)(_bstr_t)vSno, (LPSTR)(LPCSTR)_bstr_t(vName));
					    pRst->MoveNext();
					}
				}
			}
			else if (cAtion == 'A')	// ��������
			{
				dbOper.TransBegin(); // ��ʼ����
				strcpy_s(sql, "insert into test(ID, NAME) values(7, '���')");
				pRst = dbOper.ExecuteSql(sql);

				_RecordsetPtr pRst1;
				pRst1 = dbOper.ExecuteSql("insert into test(ID, NAME) values(7, '���')");

				if (NULL !=pRst && NULL != pRst1)
				{
					printf("�������ݳɹ�\n");
				}
				else
				{
					dbOper.RollbakTrans(); // �ع�����
				}
				dbOper.CheckCommit(); // ���δ�ύ�����ύ
			}
			else if (cAtion == 'D')	// ɾ������
			{
				sprintf_s(sql, "deletefrom test where id = '%d'",1);
				pRst = dbOper.ExecuteSql(sql);
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

	system("pause");
}