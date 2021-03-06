# Python stubs generated by omniidl from idl/DataBase.idl

import omniORB, _omnipy
from omniORB import CORBA, PortableServer
_0_CORBA = CORBA

_omnipy.checkVersion(3,0, __file__)


#
# Start of module "_GlobalIDL"
#
__name__ = "_GlobalIDL"
_0__GlobalIDL = omniORB.openModule("_GlobalIDL", r"idl/DataBase.idl")
_0__GlobalIDL__POA = omniORB.openModule("_GlobalIDL__POA", r"idl/DataBase.idl")


# typedef ... StringSeq
class StringSeq:
    _NP_RepositoryId = "IDL:StringSeq:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0__GlobalIDL.StringSeq = StringSeq
_0__GlobalIDL._d_StringSeq  = (omniORB.tcInternal.tv_sequence, (omniORB.tcInternal.tv_string,0), 0)
_0__GlobalIDL._ad_StringSeq = (omniORB.tcInternal.tv_alias, StringSeq._NP_RepositoryId, "StringSeq", (omniORB.tcInternal.tv_sequence, (omniORB.tcInternal.tv_string,0), 0))
_0__GlobalIDL._tc_StringSeq = omniORB.tcInternal.createTypeCode(_0__GlobalIDL._ad_StringSeq)
omniORB.registerType(StringSeq._NP_RepositoryId, _0__GlobalIDL._ad_StringSeq, _0__GlobalIDL._tc_StringSeq)
del StringSeq

#
# Start of module "DataBase"
#
__name__ = "DataBase"
_0_DataBase = omniORB.openModule("DataBase", r"idl/DataBase.idl")
_0_DataBase__POA = omniORB.openModule("DataBase__POA", r"idl/DataBase.idl")


# interface mDataBase
_0_DataBase._d_mDataBase = (omniORB.tcInternal.tv_objref, "IDL:DataBase/mDataBase:1.0", "mDataBase")
omniORB.typeMapping["IDL:DataBase/mDataBase:1.0"] = _0_DataBase._d_mDataBase
_0_DataBase.mDataBase = omniORB.newEmptyClass()
class mDataBase :
    _NP_RepositoryId = _0_DataBase._d_mDataBase[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil


_0_DataBase.mDataBase = mDataBase
_0_DataBase._tc_mDataBase = omniORB.tcInternal.createTypeCode(_0_DataBase._d_mDataBase)
omniORB.registerType(mDataBase._NP_RepositoryId, _0_DataBase._d_mDataBase, _0_DataBase._tc_mDataBase)

# mDataBase operations and attributes
mDataBase._d_setConnection = (((omniORB.tcInternal.tv_string,0), (omniORB.tcInternal.tv_string,0), (omniORB.tcInternal.tv_string,0)), (omniORB.tcInternal.tv_boolean, ), None)
mDataBase._d_executeQuery = (((omniORB.tcInternal.tv_string,0), (omniORB.tcInternal.tv_string,0), (omniORB.tcInternal.tv_string,0)), (omniORB.tcInternal.tv_boolean, ), None)
mDataBase._d_ResultSetNext = (((omniORB.tcInternal.tv_string,0), ), (omniORB.tcInternal.tv_boolean, ), None)
mDataBase._d_ResultSetPrevious = (((omniORB.tcInternal.tv_string,0), ), (omniORB.tcInternal.tv_boolean, ), None)
mDataBase._d_ResultSetFirst = (((omniORB.tcInternal.tv_string,0), ), (omniORB.tcInternal.tv_boolean, ), None)
mDataBase._d_ResultSetLast = (((omniORB.tcInternal.tv_string,0), ), (omniORB.tcInternal.tv_boolean, ), None)
mDataBase._d_ResultSetBeforeFirst = (((omniORB.tcInternal.tv_string,0), ), (omniORB.tcInternal.tv_boolean, ), None)
mDataBase._d_ResultSetAfterLast = (((omniORB.tcInternal.tv_string,0), ), (omniORB.tcInternal.tv_boolean, ), None)
mDataBase._d_getByte = (((omniORB.tcInternal.tv_string,0), omniORB.tcInternal.tv_short), (omniORB.tcInternal.tv_octet, ), None)
mDataBase._d_getShort = (((omniORB.tcInternal.tv_string,0), omniORB.tcInternal.tv_short), (omniORB.tcInternal.tv_short, ), None)
mDataBase._d_getLong = (((omniORB.tcInternal.tv_string,0), omniORB.tcInternal.tv_short), (omniORB.tcInternal.tv_long, ), None)
mDataBase._d_getFloat = (((omniORB.tcInternal.tv_string,0), omniORB.tcInternal.tv_short), (omniORB.tcInternal.tv_float, ), None)
mDataBase._d_getDouble = (((omniORB.tcInternal.tv_string,0), omniORB.tcInternal.tv_short), (omniORB.tcInternal.tv_double, ), None)
mDataBase._d_getBoolean = (((omniORB.tcInternal.tv_string,0), omniORB.tcInternal.tv_short), (omniORB.tcInternal.tv_boolean, ), None)
mDataBase._d_getString = (((omniORB.tcInternal.tv_string,0), omniORB.tcInternal.tv_short), ((omniORB.tcInternal.tv_string,0), ), None)
mDataBase._d_getDataBaseNames = ((), (omniORB.typeMapping["IDL:StringSeq:1.0"], ), None)
mDataBase._d_getDataTableNames = (((omniORB.tcInternal.tv_string,0), ), (omniORB.typeMapping["IDL:StringSeq:1.0"], ), None)
mDataBase._d_executeUpdate = (((omniORB.tcInternal.tv_string,0), (omniORB.tcInternal.tv_string,0)), (omniORB.tcInternal.tv_boolean, ), None)
mDataBase._d_getRow = (((omniORB.tcInternal.tv_string,0), ), (omniORB.tcInternal.tv_short, ), None)
mDataBase._d_AddTable = (((omniORB.tcInternal.tv_string,0), (omniORB.tcInternal.tv_string,0), omniORB.typeMapping["IDL:StringSeq:1.0"], omniORB.typeMapping["IDL:StringSeq:1.0"]), (omniORB.tcInternal.tv_boolean, ), None)
mDataBase._d_RemoveTable = (((omniORB.tcInternal.tv_string,0), (omniORB.tcInternal.tv_string,0)), (omniORB.tcInternal.tv_boolean, ), None)
mDataBase._d_AddDataBase = (((omniORB.tcInternal.tv_string,0), ), (omniORB.tcInternal.tv_boolean, ), None)
mDataBase._d_RemoveDataBase = (((omniORB.tcInternal.tv_string,0), ), (omniORB.tcInternal.tv_boolean, ), None)

# mDataBase object reference
class _objref_mDataBase (CORBA.Object):
    _NP_RepositoryId = mDataBase._NP_RepositoryId

    def __init__(self):
        CORBA.Object.__init__(self)

    def setConnection(self, *args):
        return _omnipy.invoke(self, "setConnection", _0_DataBase.mDataBase._d_setConnection, args)

    def executeQuery(self, *args):
        return _omnipy.invoke(self, "executeQuery", _0_DataBase.mDataBase._d_executeQuery, args)

    def ResultSetNext(self, *args):
        return _omnipy.invoke(self, "ResultSetNext", _0_DataBase.mDataBase._d_ResultSetNext, args)

    def ResultSetPrevious(self, *args):
        return _omnipy.invoke(self, "ResultSetPrevious", _0_DataBase.mDataBase._d_ResultSetPrevious, args)

    def ResultSetFirst(self, *args):
        return _omnipy.invoke(self, "ResultSetFirst", _0_DataBase.mDataBase._d_ResultSetFirst, args)

    def ResultSetLast(self, *args):
        return _omnipy.invoke(self, "ResultSetLast", _0_DataBase.mDataBase._d_ResultSetLast, args)

    def ResultSetBeforeFirst(self, *args):
        return _omnipy.invoke(self, "ResultSetBeforeFirst", _0_DataBase.mDataBase._d_ResultSetBeforeFirst, args)

    def ResultSetAfterLast(self, *args):
        return _omnipy.invoke(self, "ResultSetAfterLast", _0_DataBase.mDataBase._d_ResultSetAfterLast, args)

    def getByte(self, *args):
        return _omnipy.invoke(self, "getByte", _0_DataBase.mDataBase._d_getByte, args)

    def getShort(self, *args):
        return _omnipy.invoke(self, "getShort", _0_DataBase.mDataBase._d_getShort, args)

    def getLong(self, *args):
        return _omnipy.invoke(self, "getLong", _0_DataBase.mDataBase._d_getLong, args)

    def getFloat(self, *args):
        return _omnipy.invoke(self, "getFloat", _0_DataBase.mDataBase._d_getFloat, args)

    def getDouble(self, *args):
        return _omnipy.invoke(self, "getDouble", _0_DataBase.mDataBase._d_getDouble, args)

    def getBoolean(self, *args):
        return _omnipy.invoke(self, "getBoolean", _0_DataBase.mDataBase._d_getBoolean, args)

    def getString(self, *args):
        return _omnipy.invoke(self, "getString", _0_DataBase.mDataBase._d_getString, args)

    def getDataBaseNames(self, *args):
        return _omnipy.invoke(self, "getDataBaseNames", _0_DataBase.mDataBase._d_getDataBaseNames, args)

    def getDataTableNames(self, *args):
        return _omnipy.invoke(self, "getDataTableNames", _0_DataBase.mDataBase._d_getDataTableNames, args)

    def executeUpdate(self, *args):
        return _omnipy.invoke(self, "executeUpdate", _0_DataBase.mDataBase._d_executeUpdate, args)

    def getRow(self, *args):
        return _omnipy.invoke(self, "getRow", _0_DataBase.mDataBase._d_getRow, args)

    def AddTable(self, *args):
        return _omnipy.invoke(self, "AddTable", _0_DataBase.mDataBase._d_AddTable, args)

    def RemoveTable(self, *args):
        return _omnipy.invoke(self, "RemoveTable", _0_DataBase.mDataBase._d_RemoveTable, args)

    def AddDataBase(self, *args):
        return _omnipy.invoke(self, "AddDataBase", _0_DataBase.mDataBase._d_AddDataBase, args)

    def RemoveDataBase(self, *args):
        return _omnipy.invoke(self, "RemoveDataBase", _0_DataBase.mDataBase._d_RemoveDataBase, args)

    __methods__ = ["setConnection", "executeQuery", "ResultSetNext", "ResultSetPrevious", "ResultSetFirst", "ResultSetLast", "ResultSetBeforeFirst", "ResultSetAfterLast", "getByte", "getShort", "getLong", "getFloat", "getDouble", "getBoolean", "getString", "getDataBaseNames", "getDataTableNames", "executeUpdate", "getRow", "AddTable", "RemoveTable", "AddDataBase", "RemoveDataBase"] + CORBA.Object.__methods__

omniORB.registerObjref(mDataBase._NP_RepositoryId, _objref_mDataBase)
_0_DataBase._objref_mDataBase = _objref_mDataBase
del mDataBase, _objref_mDataBase

# mDataBase skeleton
__name__ = "DataBase__POA"
class mDataBase (PortableServer.Servant):
    _NP_RepositoryId = _0_DataBase.mDataBase._NP_RepositoryId


    _omni_op_d = {"setConnection": _0_DataBase.mDataBase._d_setConnection, "executeQuery": _0_DataBase.mDataBase._d_executeQuery, "ResultSetNext": _0_DataBase.mDataBase._d_ResultSetNext, "ResultSetPrevious": _0_DataBase.mDataBase._d_ResultSetPrevious, "ResultSetFirst": _0_DataBase.mDataBase._d_ResultSetFirst, "ResultSetLast": _0_DataBase.mDataBase._d_ResultSetLast, "ResultSetBeforeFirst": _0_DataBase.mDataBase._d_ResultSetBeforeFirst, "ResultSetAfterLast": _0_DataBase.mDataBase._d_ResultSetAfterLast, "getByte": _0_DataBase.mDataBase._d_getByte, "getShort": _0_DataBase.mDataBase._d_getShort, "getLong": _0_DataBase.mDataBase._d_getLong, "getFloat": _0_DataBase.mDataBase._d_getFloat, "getDouble": _0_DataBase.mDataBase._d_getDouble, "getBoolean": _0_DataBase.mDataBase._d_getBoolean, "getString": _0_DataBase.mDataBase._d_getString, "getDataBaseNames": _0_DataBase.mDataBase._d_getDataBaseNames, "getDataTableNames": _0_DataBase.mDataBase._d_getDataTableNames, "executeUpdate": _0_DataBase.mDataBase._d_executeUpdate, "getRow": _0_DataBase.mDataBase._d_getRow, "AddTable": _0_DataBase.mDataBase._d_AddTable, "RemoveTable": _0_DataBase.mDataBase._d_RemoveTable, "AddDataBase": _0_DataBase.mDataBase._d_AddDataBase, "RemoveDataBase": _0_DataBase.mDataBase._d_RemoveDataBase}

mDataBase._omni_skeleton = mDataBase
_0_DataBase__POA.mDataBase = mDataBase
omniORB.registerSkeleton(mDataBase._NP_RepositoryId, mDataBase)
del mDataBase
__name__ = "DataBase"

#
# End of module "DataBase"
#
__name__ = "_GlobalIDL"


#
# End of module "_GlobalIDL"
#
__name__ = "DataBase_idl"

_exported_modules = ( "DataBase", "_GlobalIDL")

# The end.
