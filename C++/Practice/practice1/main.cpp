// ConsoleApplication2.cpp: 콘솔 응용 프로그램의 진입점을 정의합니다.
//

#include "stdafx.h" 
#include "CMyString.h"


int main()
{
	CMyString strData;
	strData.SetString("Hello");
	cout << strData.GetString() << endl;
    return 0;
}

