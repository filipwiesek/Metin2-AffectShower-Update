// find:
#ifdef ENABLE_NEW_EQUIPMENT_SYSTEM
	PyModule_AddIntConstant(poModule, "ENABLE_NEW_EQUIPMENT_SYSTEM",	1);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_NEW_EQUIPMENT_SYSTEM",	0);
#endif

// paste below:
#ifdef ENABLE_AFFECT_FIX
	PyModule_AddIntConstant(poModule, "ENABLE_AFFECT_FIX", 1);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_AFFECT_FIX", 0);
#endif
