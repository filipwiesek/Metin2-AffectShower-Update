// find:
void CPythonNetworkStream::__RefreshEquipmentWindow()
{
	m_isRefreshEquipmentWnd=true;
}

// paste below:
#ifdef ENABLE_AFFECT_FIX
void CPythonNetworkStream::__RefreshAffectWindow()
{
	m_isRefreshAffectWindow = true;
}
#endif

// find:
	if (m_isRefreshGuildWndGradePage)
	{
		m_isRefreshGuildWndGradePage=false;
		PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "RefreshGuildGradePage", Py_BuildValue("()"));
		s_nextRefreshTime = curTime + 300;
	}

// paste below:
#ifdef ENABLE_AFFECT_FIX
	if (m_isRefreshAffectWindow)
	{
		m_isRefreshAffectWindow = false;
		PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "RefreshAffectWindow", Py_BuildValue("()"));
		s_nextRefreshTime = curTime + 300;
	}
#endif

// find:
	m_isRefreshGuildWndGradePage=false;

// paste below:
#ifdef ENABLE_AFFECT_FIX
	m_isRefreshAffectWindow = false;
#endif

// find:
	PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "BINARY_NEW_AddAffect", Py_BuildValue("(iiii)", rkElement.dwType, rkElement.bPointIdxApplyOn, rkElement.lApplyValue, rkElement.lDuration));

// paste below:
#ifdef ENABLE_AFFECT_FIX
	__RefreshAffectWindow();
#endif

// find:
	PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "BINARY_NEW_RemoveAffect", Py_BuildValue("(ii)", kAffectRemove.dwType, kAffectRemove.bApplyOn));

// paste below:
#ifdef ENABLE_AFFECT_FIX
	__RefreshAffectWindow();
#endif
