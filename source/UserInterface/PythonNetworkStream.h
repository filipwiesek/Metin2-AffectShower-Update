// find:
		void __RefreshMallWindow();

// paste below:
#ifdef ENABLE_AFFECT_FIX
		void __RefreshAffectWindow();
#endif

// find:
		bool m_isRefreshGuildWndGradePage;

// paste below:
#ifdef ENABLE_AFFECT_FIX
		bool m_isRefreshAffectWindow;
#endif
