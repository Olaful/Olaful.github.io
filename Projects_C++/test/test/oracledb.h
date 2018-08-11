
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
	DBOper(char *szUserID, char *szPwd);
    ~DBOper();

    //���������ݿ�
    bool ConnToDB(char *strConn,char *szUserID, char*szPwd);
 
    //���ݿ��������
    //��ѯ����ɾ���Լ����
    _RecordsetPtr ExecuteSql(const string strSql);

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

	// ���ݹؼ��ֻ�ȡ��Ӧ�ֶ�ֵ
	//template <typename T>
	//void GetValue(char *szKey, T &result);
	void GetValue(char *szKey, int &nValue) // ����ʵ���൱���Զ�������
	{
		_variant_t varResult;
		varResult = m_pRst->GetCollect(_variant_t(szKey));
		nValue = varResult.intVal;
	}
	
	inline void GetValue(char *szKey, char *szValue) // inlineֻ�ڵ�ǰ��Ԫ��Ч,���Բ�����CPP�ļ���ʵ��
	{
		_variant_t varResult;
		varResult = m_pRst->GetCollect(_variant_t(szKey));
		strcpy(szValue, (LPSTR)(LPCSTR)_bstr_t(varResult));
	}
	
	inline void GetValue(char *szKey, float &fValue)
	{
		_variant_t varResult;
		varResult = m_pRst->GetCollect(_variant_t(szKey));
		fValue = varResult.fltVal;
	}
	
	inline void GetValue(char *szKey, double &dValue)
	{
		_variant_t varResult;
		varResult = m_pRst->GetCollect(_variant_t(szKey));
		dValue = varResult.dblVal;
	}
	
	inline void GetValue(char *szKey, string &strValue)
	{
		_variant_t varResult;
		varResult = m_pRst->GetCollect(_variant_t(szKey));
		strValue = varResult.pcVal;
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