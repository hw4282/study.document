#include "stdafx.h"
#include "CMyString.h"


CMyString::CMyString()
	: m_pszData(NULL) 
	, m_nLength(0)
{
}

CMyString::~CMyString()
{
	Release();
}


int CMyString::SetString(const char* pszParam)
{
	Release();

	if (pszParam == NULL)
		return 0;

	int nLength = strlen(pszParam);
	cout << "Length = "<< nLength << endl;

	if (m_nLength == 0)
		return 0;
	m_pszData = new char[m_nLength + 1];

	strcpy_s(m_pszData, sizeof(char)* (nLength + 1), pszParam);
	m_nLength = nLength;

	
	return nLength;
}


const char* CMyString::GetString(void)
{
	return m_pszData;
}


void CMyString::Release()
{
	if (m_pszData != NULL)
		delete[] m_pszData;

	m_pszData = NULL;
	m_nLength = 0;
}