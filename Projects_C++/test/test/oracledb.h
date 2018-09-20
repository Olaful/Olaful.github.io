
#pragma once
//pragma �趨��������״̬��ָʾ���������һЩ�ض��Ķ���
#import "C:\Program Files\Common Files\System\ado\msado15.dll" no_namespace rename("EOF","adoEOF")
//������������#import���ʱ������Ϊ����������Ϳ��еĽӿ����ɰ�װ�࣬#import���ʵ�����൱��ִ����API����LoadTypeLib()��
//#import�����ڹ��̿�ִ�г������Ŀ¼�в��������ļ����ֱ�Ϊ*.tlh(���Ϳ�ͷ�ļ�)��*.tli(���Ϳ�ʵ���ļ�)��
//���Ƿֱ�Ϊÿһ���ӿڲ�������ָ�룬��Ϊ���ֽӿڷ�����ö�����ͣ�CLSID�Ƚ�������������һϵ�а�װ������
//��û�о�������������֮ǰ���ļ���û�����ɣ����ԣ�����ִ�����ʾ��

#define PI 3.14
//#define MAX (x > y ? x : y)

#include<string>
using namespace std;

class DBOper
{
public:
	//��ʼ�����ݿ������Ҫ�Ķ���
	DBOper();
	DBOper(const char *szUserID, const char *szPwd);
	~DBOper();

	//���������ݿ�
	bool ConnToDB(const char *strConn, const char *szUserID, const char*szPwd);

	//���ݿ��������
	//��ѯ����ɾ���Լ����
	void ExecuteSql(const string strSql);

	// ��������
	void TransBegin();

	// �ύ����
	void CheckCommit();

	// �ع�����
	void RollbakTrans();

	// ��sql���
	void Open(string strSql);

	// ִ��sql
	void Execute();

	// �������
	void SetValue();

	// ������Ƿ�Ϊ��
	bool Eof();

	void Close();

	// ������ƶ�����һ��
	void MoveNext();

	int RecordCnt();

	// ���ݹؼ��ֻ�ȡ��Ӧ�ֶ�ֵ
	//template <typename T>
	//void GetValue(char *szKey, T &result);
	// ����ʵ���൱���Զ�������
	void GetValue(const char *szKey, int &nValue)
	{
		_variant_t varResult;
		varResult = m_pRst->GetCollect(_variant_t(szKey));
		nValue = varResult.intVal;
	}

	// inlineֻ�ڵ�ǰ��Ԫ��Ч,���Բ�����CPP�ļ���ʵ��
	inline void GetValue(const char *szKey, char *szValue)
	{
		_variant_t varResult;
		varResult = m_pRst->GetCollect(_variant_t(szKey));
		strcpy(szValue, (LPSTR)(LPCSTR)_bstr_t(varResult));
	}

	inline void GetValue(const char *szKey, float &fValue)
	{
		_variant_t varResult;
		varResult = m_pRst->GetCollect(_variant_t(szKey));
		fValue = varResult.fltVal;
	}

	inline void GetValue(const char *szKey, double &dValue)
	{
		_variant_t varResult;
		varResult = m_pRst->GetCollect(_variant_t(szKey));
		dValue = varResult.dblVal;
	}

	inline void GetValue(const char *szKey, string &strValue)
	{
		_variant_t varResult;
		varResult = m_pRst->GetCollect(_variant_t(szKey));
		strValue = (LPSTR)(LPCSTR)_bstr_t(varResult);
	}

private:
	// ��ӡ���Ӵ�����Ϣ
	void PrintErrorInfo(_com_error &);

private:
	//��ʼ�����ݿ����ӡ������¼��
	_ConnectionPtr CreateConnPtr();
	_CommandPtr CreateCommPtr();
	//_RecordsetPtr CreateRecsetPtr();

private:
	//���ݿ�������Ҫ�����ӡ������������
	_ConnectionPtr m_pConnection;
	_CommandPtr m_pCommand;

private:
	// �Ƿ��Ѿ��ع������־
	char m_cRollbackFlag;

	// ��ִ�е�sql���
	string m_strSql;

	// �����
	_RecordsetPtr m_pRst;
};

class myDbException : public exception
{
public:
	virtual const char* what() const throw()
	{
		return szErrorMsg;
	}

	myDbException(const char* szMsg)
	{
		strcpy_s(szErrorMsg, szMsg);
	}

private:
	char szErrorMsg[1024];
};