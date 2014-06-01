# PySNMP SMI module. Autogenerated from smidump -f python SNMP-USER-BASED-SM-MIB
# by libsmi2pysnmp-0.1.3 at Tue Apr  3 16:13:22 2012,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( SnmpAdminString, SnmpEngineID, snmpAuthProtocols, snmpPrivProtocols, ) = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString", "SnmpEngineID", "snmpAuthProtocols", "snmpPrivProtocols")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Counter32, Integer32, ModuleIdentity, MibIdentifier, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, snmpModules, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Integer32", "ModuleIdentity", "MibIdentifier", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "snmpModules")
( AutonomousType, RowPointer, RowStatus, StorageType, TextualConvention, TestAndIncr, ) = mibBuilder.importSymbols("SNMPv2-TC", "AutonomousType", "RowPointer", "RowStatus", "StorageType", "TextualConvention", "TestAndIncr")

# Types

class KeyChange(OctetString):
    pass


# Objects

usmNoAuthProtocol = ObjectIdentity((1, 3, 6, 1, 6, 3, 10, 1, 1, 1))
if mibBuilder.loadTexts: usmNoAuthProtocol.setDescription("No Authentication Protocol.")
usmHMACMD5AuthProtocol = ObjectIdentity((1, 3, 6, 1, 6, 3, 10, 1, 1, 2))
if mibBuilder.loadTexts: usmHMACMD5AuthProtocol.setDescription("The HMAC-MD5-96 Digest Authentication Protocol.")
usmHMACSHAAuthProtocol = ObjectIdentity((1, 3, 6, 1, 6, 3, 10, 1, 1, 3))
if mibBuilder.loadTexts: usmHMACSHAAuthProtocol.setDescription("The HMAC-SHA-96 Digest Authentication Protocol.")
usmNoPrivProtocol = ObjectIdentity((1, 3, 6, 1, 6, 3, 10, 1, 2, 1))
if mibBuilder.loadTexts: usmNoPrivProtocol.setDescription("No Privacy Protocol.")
usmDESPrivProtocol = ObjectIdentity((1, 3, 6, 1, 6, 3, 10, 1, 2, 2))
if mibBuilder.loadTexts: usmDESPrivProtocol.setDescription("The CBC-DES Symmetric Encryption Protocol.")
snmpUsmMIB = ModuleIdentity((1, 3, 6, 1, 6, 3, 15)).setRevisions(("2002-10-16 00:00","1999-01-20 00:00","1997-11-20 00:00",))
if mibBuilder.loadTexts: snmpUsmMIB.setOrganization("SNMPv3 Working Group")
if mibBuilder.loadTexts: snmpUsmMIB.setContactInfo("WG-email:   snmpv3@lists.tislabs.com\nSubscribe:  majordomo@lists.tislabs.com\n            In msg body:  subscribe snmpv3\n\nChair:      Russ Mundy\n            Network Associates Laboratories\npostal:     15204 Omega Drive, Suite 300\n            Rockville, MD 20850-4601\n            USA\nemail:      mundy@tislabs.com\n\nphone:      +1 301-947-7107\n\nCo-Chair:   David Harrington\n            Enterasys Networks\nPostal:     35 Industrial Way\n            P. O. Box 5004\n            Rochester, New Hampshire 03866-5005\n            USA\nEMail:      dbh@enterasys.com\nPhone:      +1 603-337-2614\n\nCo-editor   Uri Blumenthal\n            Lucent Technologies\npostal:     67 Whippany Rd.\n            Whippany, NJ 07981\n            USA\nemail:      uri@lucent.com\nphone:      +1-973-386-2163\n\nCo-editor:  Bert Wijnen\n            Lucent Technologies\npostal:     Schagen 33\n            3461 GL Linschoten\n            Netherlands\nemail:      bwijnen@lucent.com\nphone:      +31-348-480-685")
if mibBuilder.loadTexts: snmpUsmMIB.setDescription("The management information definitions for the\nSNMP User-based Security Model.\n\nCopyright (C) The Internet Society (2002). This\nversion of this MIB module is part of RFC 3414;\nsee the RFC itself for full legal notices.")
usmMIBObjects = MibIdentifier((1, 3, 6, 1, 6, 3, 15, 1))
usmStats = MibIdentifier((1, 3, 6, 1, 6, 3, 15, 1, 1))
usmStatsUnsupportedSecLevels = MibScalar((1, 3, 6, 1, 6, 3, 15, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usmStatsUnsupportedSecLevels.setDescription("The total number of packets received by the SNMP\nengine which were dropped because they requested a\nsecurityLevel that was unknown to the SNMP engine\nor otherwise unavailable.")
usmStatsNotInTimeWindows = MibScalar((1, 3, 6, 1, 6, 3, 15, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usmStatsNotInTimeWindows.setDescription("The total number of packets received by the SNMP\nengine which were dropped because they appeared\noutside of the authoritative SNMP engine's window.")
usmStatsUnknownUserNames = MibScalar((1, 3, 6, 1, 6, 3, 15, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usmStatsUnknownUserNames.setDescription("The total number of packets received by the SNMP\nengine which were dropped because they referenced a\nuser that was not known to the SNMP engine.")
usmStatsUnknownEngineIDs = MibScalar((1, 3, 6, 1, 6, 3, 15, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usmStatsUnknownEngineIDs.setDescription("The total number of packets received by the SNMP\nengine which were dropped because they referenced an\nsnmpEngineID that was not known to the SNMP engine.")
usmStatsWrongDigests = MibScalar((1, 3, 6, 1, 6, 3, 15, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usmStatsWrongDigests.setDescription("The total number of packets received by the SNMP\nengine which were dropped because they didn't\ncontain the expected digest value.")
usmStatsDecryptionErrors = MibScalar((1, 3, 6, 1, 6, 3, 15, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usmStatsDecryptionErrors.setDescription("The total number of packets received by the SNMP\nengine which were dropped because they could not be\ndecrypted.")
usmUser = MibIdentifier((1, 3, 6, 1, 6, 3, 15, 1, 2))
usmUserSpinLock = MibScalar((1, 3, 6, 1, 6, 3, 15, 1, 2, 1), TestAndIncr()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: usmUserSpinLock.setDescription("An advisory lock used to allow several cooperating\nCommand Generator Applications to coordinate their\nuse of facilities to alter secrets in the\nusmUserTable.")
usmUserTable = MibTable((1, 3, 6, 1, 6, 3, 15, 1, 2, 2))
if mibBuilder.loadTexts: usmUserTable.setDescription("The table of users configured in the SNMP engine's\nLocal Configuration Datastore (LCD).\n\nTo create a new user (i.e., to instantiate a new\nconceptual row in this table), it is recommended to\nfollow this procedure:\n\n  1)  GET(usmUserSpinLock.0) and save in sValue.\n\n  2)  SET(usmUserSpinLock.0=sValue,\n          usmUserCloneFrom=templateUser,\n          usmUserStatus=createAndWait)\n      You should use a template user to clone from\n      which has the proper auth/priv protocol defined.\n\nIf the new user is to use privacy:\n\n  3)  generate the keyChange value based on the secret\n      privKey of the clone-from user and the secret key\n      to be used for the new user. Let us call this\n      pkcValue.\n  4)  GET(usmUserSpinLock.0) and save in sValue.\n  5)  SET(usmUserSpinLock.0=sValue,\n          usmUserPrivKeyChange=pkcValue\n          usmUserPublic=randomValue1)\n  6)  GET(usmUserPulic) and check it has randomValue1.\n      If not, repeat steps 4-6.\n\nIf the new user will never use privacy:\n\n  7)  SET(usmUserPrivProtocol=usmNoPrivProtocol)\n\nIf the new user is to use authentication:\n\n  8)  generate the keyChange value based on the secret\n      authKey of the clone-from user and the secret key\n      to be used for the new user. Let us call this\n      akcValue.\n  9)  GET(usmUserSpinLock.0) and save in sValue.\n  10) SET(usmUserSpinLock.0=sValue,\n          usmUserAuthKeyChange=akcValue\n          usmUserPublic=randomValue2)\n  11) GET(usmUserPulic) and check it has randomValue2.\n      If not, repeat steps 9-11.\n\nIf the new user will never use authentication:\n\n  12) SET(usmUserAuthProtocol=usmNoAuthProtocol)\n\nFinally, activate the new user:\n\n  13) SET(usmUserStatus=active)\n\nThe new user should now be available and ready to be\nused for SNMPv3 communication. Note however that access\nto MIB data must be provided via configuration of the\nSNMP-VIEW-BASED-ACM-MIB.\n\nThe use of usmUserSpinlock is to avoid conflicts with\nanother SNMP command generator application which may\nalso be acting on the usmUserTable.")
usmUserEntry = MibTableRow((1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1)).setIndexNames((0, "SNMP-USER-BASED-SM-MIB", "usmUserEngineID"), (0, "SNMP-USER-BASED-SM-MIB", "usmUserName"))
if mibBuilder.loadTexts: usmUserEntry.setDescription("A user configured in the SNMP engine's Local\nConfiguration Datastore (LCD) for the User-based\nSecurity Model.")
usmUserEngineID = MibTableColumn((1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 1), SnmpEngineID()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: usmUserEngineID.setDescription("An SNMP engine's administratively-unique identifier.\n\nIn a simple agent, this value is always that agent's\nown snmpEngineID value.\n\nThe value can also take the value of the snmpEngineID\nof a remote SNMP engine with which this user can\ncommunicate.")
usmUserName = MibTableColumn((1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: usmUserName.setDescription("A human readable string representing the name of\nthe user.\n\nThis is the (User-based Security) Model dependent\nsecurity ID.")
usmUserSecurityName = MibTableColumn((1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 3), SnmpAdminString()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: usmUserSecurityName.setDescription("A human readable string representing the user in\nSecurity Model independent format.\n\nThe default transformation of the User-based Security\nModel dependent security ID to the securityName and\nvice versa is the identity function so that the\nsecurityName is the same as the userName.")
usmUserCloneFrom = MibTableColumn((1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 4), RowPointer((0,0))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usmUserCloneFrom.setDescription("A pointer to another conceptual row in this\nusmUserTable.  The user in this other conceptual\nrow is called the clone-from user.\n\nWhen a new user is created (i.e., a new conceptual\nrow is instantiated in this table), the privacy and\nauthentication parameters of the new user must be\ncloned from its clone-from user. These parameters are:\n  - authentication protocol (usmUserAuthProtocol)\n  - privacy protocol (usmUserPrivProtocol)\nThey will be copied regardless of what the current\nvalue is.\n\nCloning also causes the initial values of the secret\nauthentication key (authKey) and the secret encryption\n\nkey (privKey) of the new user to be set to the same\nvalues as the corresponding secrets of the clone-from\nuser to allow the KeyChange process to occur as\nrequired during user creation.\n\nThe first time an instance of this object is set by\na management operation (either at or after its\ninstantiation), the cloning process is invoked.\nSubsequent writes are successful but invoke no\naction to be taken by the receiver.\nThe cloning process fails with an 'inconsistentName'\nerror if the conceptual row representing the\nclone-from user does not exist or is not in an active\nstate when the cloning process is invoked.\n\nWhen this object is read, the ZeroDotZero OID\nis returned.")
usmUserAuthProtocol = MibTableColumn((1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 5), AutonomousType().clone('1.3.6.1.6.3.10.1.1.1')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usmUserAuthProtocol.setDescription("An indication of whether messages sent on behalf of\nthis user to/from the SNMP engine identified by\nusmUserEngineID, can be authenticated, and if so,\nthe type of authentication protocol which is used.\n\nAn instance of this object is created concurrently\nwith the creation of any other object instance for\nthe same user (i.e., as part of the processing of\nthe set operation which creates the first object\ninstance in the same conceptual row).\n\nIf an initial set operation (i.e. at row creation time)\ntries to set a value for an unknown or unsupported\nprotocol, then a 'wrongValue' error must be returned.\n\nThe value will be overwritten/set when a set operation\nis performed on the corresponding instance of\nusmUserCloneFrom.\n\nOnce instantiated, the value of such an instance of\nthis object can only be changed via a set operation to\nthe value of the usmNoAuthProtocol.\n\nIf a set operation tries to change the value of an\n\nexisting instance of this object to any value other\nthan usmNoAuthProtocol, then an 'inconsistentValue'\nerror must be returned.\n\nIf a set operation tries to set the value to the\nusmNoAuthProtocol while the usmUserPrivProtocol value\nin the same row is not equal to usmNoPrivProtocol,\nthen an 'inconsistentValue' error must be returned.\nThat means that an SNMP command generator application\nmust first ensure that the usmUserPrivProtocol is set\nto the usmNoPrivProtocol value before it can set\nthe usmUserAuthProtocol value to usmNoAuthProtocol.")
usmUserAuthKeyChange = MibTableColumn((1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 6), KeyChange().clone('')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usmUserAuthKeyChange.setDescription("An object, which when modified, causes the secret\nauthentication key used for messages sent on behalf\nof this user to/from the SNMP engine identified by\nusmUserEngineID, to be modified via a one-way\nfunction.\n\nThe associated protocol is the usmUserAuthProtocol.\nThe associated secret key is the user's secret\nauthentication key (authKey). The associated hash\nalgorithm is the algorithm used by the user's\nusmUserAuthProtocol.\n\nWhen creating a new user, it is an 'inconsistentName'\nerror for a set operation to refer to this object\nunless it is previously or concurrently initialized\nthrough a set operation on the corresponding instance\nof usmUserCloneFrom.\n\nWhen the value of the corresponding usmUserAuthProtocol\nis usmNoAuthProtocol, then a set is successful, but\neffectively is a no-op.\n\nWhen this object is read, the zero-length (empty)\nstring is returned.\n\nThe recommended way to do a key change is as follows:\n\n  1) GET(usmUserSpinLock.0) and save in sValue.\n  2) generate the keyChange value based on the old\n     (existing) secret key and the new secret key,\n     let us call this kcValue.\n\nIf you do the key change on behalf of another user:\n\n  3) SET(usmUserSpinLock.0=sValue,\n         usmUserAuthKeyChange=kcValue\n         usmUserPublic=randomValue)\n\nIf you do the key change for yourself:\n\n  4) SET(usmUserSpinLock.0=sValue,\n         usmUserOwnAuthKeyChange=kcValue\n         usmUserPublic=randomValue)\n\nIf you get a response with error-status of noError,\nthen the SET succeeded and the new key is active.\nIf you do not get a response, then you can issue a\nGET(usmUserPublic) and check if the value is equal\nto the randomValue you did send in the SET. If so, then\nthe key change succeeded and the new key is active\n(probably the response got lost). If not, then the SET\nrequest probably never reached the target and so you\ncan start over with the procedure above.")
usmUserOwnAuthKeyChange = MibTableColumn((1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 7), KeyChange().clone('')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usmUserOwnAuthKeyChange.setDescription("Behaves exactly as usmUserAuthKeyChange, with one\nnotable difference: in order for the set operation\nto succeed, the usmUserName of the operation\nrequester must match the usmUserName that\nindexes the row which is targeted by this\noperation.\nIn addition, the USM security model must be\nused for this operation.\n\nThe idea here is that access to this column can be\npublic, since it will only allow a user to change\nhis own secret authentication key (authKey).\nNote that this can only be done once the row is active.\n\nWhen a set is received and the usmUserName of the\nrequester is not the same as the umsUserName that\nindexes the row which is targeted by this operation,\nthen a 'noAccess' error must be returned.\n\nWhen a set is received and the security model in use\nis not USM, then a 'noAccess' error must be returned.")
usmUserPrivProtocol = MibTableColumn((1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 8), AutonomousType().clone('1.3.6.1.6.3.10.1.2.1')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usmUserPrivProtocol.setDescription("An indication of whether messages sent on behalf of\nthis user to/from the SNMP engine identified by\nusmUserEngineID, can be protected from disclosure,\nand if so, the type of privacy protocol which is used.\n\nAn instance of this object is created concurrently\nwith the creation of any other object instance for\nthe same user (i.e., as part of the processing of\nthe set operation which creates the first object\ninstance in the same conceptual row).\n\nIf an initial set operation (i.e. at row creation time)\ntries to set a value for an unknown or unsupported\nprotocol, then a 'wrongValue' error must be returned.\n\nThe value will be overwritten/set when a set operation\nis performed on the corresponding instance of\nusmUserCloneFrom.\n\nOnce instantiated, the value of such an instance of\nthis object can only be changed via a set operation to\nthe value of the usmNoPrivProtocol.\n\nIf a set operation tries to change the value of an\nexisting instance of this object to any value other\nthan usmNoPrivProtocol, then an 'inconsistentValue'\nerror must be returned.\n\nNote that if any privacy protocol is used, then you\nmust also use an authentication protocol. In other\nwords, if usmUserPrivProtocol is set to anything else\nthan usmNoPrivProtocol, then the corresponding instance\nof usmUserAuthProtocol cannot have a value of\n\nusmNoAuthProtocol. If it does, then an\n'inconsistentValue' error must be returned.")
usmUserPrivKeyChange = MibTableColumn((1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 9), KeyChange().clone('')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usmUserPrivKeyChange.setDescription("An object, which when modified, causes the secret\nencryption key used for messages sent on behalf\nof this user to/from the SNMP engine identified by\nusmUserEngineID, to be modified via a one-way\nfunction.\n\nThe associated protocol is the usmUserPrivProtocol.\nThe associated secret key is the user's secret\nprivacy key (privKey). The associated hash\nalgorithm is the algorithm used by the user's\nusmUserAuthProtocol.\n\nWhen creating a new user, it is an 'inconsistentName'\nerror for a set operation to refer to this object\nunless it is previously or concurrently initialized\nthrough a set operation on the corresponding instance\nof usmUserCloneFrom.\n\nWhen the value of the corresponding usmUserPrivProtocol\nis usmNoPrivProtocol, then a set is successful, but\neffectively is a no-op.\n\nWhen this object is read, the zero-length (empty)\nstring is returned.\nSee the description clause of usmUserAuthKeyChange for\na recommended procedure to do a key change.")
usmUserOwnPrivKeyChange = MibTableColumn((1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 10), KeyChange().clone('')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usmUserOwnPrivKeyChange.setDescription("Behaves exactly as usmUserPrivKeyChange, with one\nnotable difference: in order for the Set operation\nto succeed, the usmUserName of the operation\nrequester must match the usmUserName that indexes\n\nthe row which is targeted by this operation.\nIn addition, the USM security model must be\nused for this operation.\n\nThe idea here is that access to this column can be\npublic, since it will only allow a user to change\nhis own secret privacy key (privKey).\nNote that this can only be done once the row is active.\n\nWhen a set is received and the usmUserName of the\nrequester is not the same as the umsUserName that\nindexes the row which is targeted by this operation,\nthen a 'noAccess' error must be returned.\n\nWhen a set is received and the security model in use\nis not USM, then a 'noAccess' error must be returned.")
usmUserPublic = MibTableColumn((1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 11), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)).clone('')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usmUserPublic.setDescription("A publicly-readable value which can be written as part\nof the procedure for changing a user's secret\nauthentication and/or privacy key, and later read to\ndetermine whether the change of the secret was\neffected.")
usmUserStorageType = MibTableColumn((1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 12), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usmUserStorageType.setDescription("The storage type for this conceptual row.\n\nConceptual rows having the value 'permanent' must\nallow write-access at a minimum to:\n\n- usmUserAuthKeyChange, usmUserOwnAuthKeyChange\n  and usmUserPublic for a user who employs\n  authentication, and\n- usmUserPrivKeyChange, usmUserOwnPrivKeyChange\n  and usmUserPublic for a user who employs\n  privacy.\n\nNote that any user who employs authentication or\nprivacy must allow its secret(s) to be updated and\nthus cannot be 'readOnly'.\n\nIf an initial set operation tries to set the value to\n'readOnly' for a user who employs authentication or\nprivacy, then an 'inconsistentValue' error must be\nreturned.  Note that if the value has been previously\nset (implicit or explicit) to any value, then the rules\nas defined in the StorageType Textual Convention apply.\n\nIt is an implementation issue to decide if a SET for\na readOnly or permanent row is accepted at all. In some\ncontexts this may make sense, in others it may not. If\na SET for a readOnly or permanent row is not accepted\nat all, then a 'wrongValue' error must be returned.")
usmUserStatus = MibTableColumn((1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 13), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usmUserStatus.setDescription("The status of this conceptual row.\n\nUntil instances of all corresponding columns are\nappropriately configured, the value of the\ncorresponding instance of the usmUserStatus column\nis 'notReady'.\n\nIn particular, a newly created row for a user who\nemploys authentication, cannot be made active until the\ncorresponding usmUserCloneFrom and usmUserAuthKeyChange\nhave been set.\n\nFurther, a newly created row for a user who also\nemploys privacy, cannot be made active until the\nusmUserPrivKeyChange has been set.\n\nThe RowStatus TC [RFC2579] requires that this\nDESCRIPTION clause states under which circumstances\nother objects in this row can be modified:\n\nThe value of this object has no effect on whether\nother objects in this conceptual row can be modified,\nexcept for usmUserOwnAuthKeyChange and\nusmUserOwnPrivKeyChange. For these 2 objects, the\n\nvalue of usmUserStatus MUST be active.")
usmMIBConformance = MibIdentifier((1, 3, 6, 1, 6, 3, 15, 2))
usmMIBCompliances = MibIdentifier((1, 3, 6, 1, 6, 3, 15, 2, 1))
usmMIBGroups = MibIdentifier((1, 3, 6, 1, 6, 3, 15, 2, 2))

# Augmentions

# Groups

usmMIBBasicGroup = ObjectGroup((1, 3, 6, 1, 6, 3, 15, 2, 2, 1)).setObjects(*(("SNMP-USER-BASED-SM-MIB", "usmStatsUnknownEngineIDs"), ("SNMP-USER-BASED-SM-MIB", "usmUserOwnAuthKeyChange"), ("SNMP-USER-BASED-SM-MIB", "usmStatsNotInTimeWindows"), ("SNMP-USER-BASED-SM-MIB", "usmStatsUnknownUserNames"), ("SNMP-USER-BASED-SM-MIB", "usmUserSecurityName"), ("SNMP-USER-BASED-SM-MIB", "usmStatsUnsupportedSecLevels"), ("SNMP-USER-BASED-SM-MIB", "usmStatsDecryptionErrors"), ("SNMP-USER-BASED-SM-MIB", "usmUserStatus"), ("SNMP-USER-BASED-SM-MIB", "usmUserPrivKeyChange"), ("SNMP-USER-BASED-SM-MIB", "usmUserOwnPrivKeyChange"), ("SNMP-USER-BASED-SM-MIB", "usmUserStorageType"), ("SNMP-USER-BASED-SM-MIB", "usmUserSpinLock"), ("SNMP-USER-BASED-SM-MIB", "usmUserAuthKeyChange"), ("SNMP-USER-BASED-SM-MIB", "usmUserCloneFrom"), ("SNMP-USER-BASED-SM-MIB", "usmUserPrivProtocol"), ("SNMP-USER-BASED-SM-MIB", "usmUserAuthProtocol"), ("SNMP-USER-BASED-SM-MIB", "usmStatsWrongDigests"), ("SNMP-USER-BASED-SM-MIB", "usmUserPublic"), ) )
if mibBuilder.loadTexts: usmMIBBasicGroup.setDescription("A collection of objects providing for configuration\nof an SNMP engine which implements the SNMP\nUser-based Security Model.")

# Compliances

usmMIBCompliance = ModuleCompliance((1, 3, 6, 1, 6, 3, 15, 2, 1, 1)).setObjects(*(("SNMP-USER-BASED-SM-MIB", "usmMIBBasicGroup"), ) )
if mibBuilder.loadTexts: usmMIBCompliance.setDescription("The compliance statement for SNMP engines which\nimplement the SNMP-USER-BASED-SM-MIB.")

# Exports

# Module identity
mibBuilder.exportSymbols("SNMP-USER-BASED-SM-MIB", PYSNMP_MODULE_ID=snmpUsmMIB)

# Types
mibBuilder.exportSymbols("SNMP-USER-BASED-SM-MIB", KeyChange=KeyChange)

# Objects
mibBuilder.exportSymbols("SNMP-USER-BASED-SM-MIB", usmNoAuthProtocol=usmNoAuthProtocol, usmHMACMD5AuthProtocol=usmHMACMD5AuthProtocol, usmHMACSHAAuthProtocol=usmHMACSHAAuthProtocol, usmNoPrivProtocol=usmNoPrivProtocol, usmDESPrivProtocol=usmDESPrivProtocol, snmpUsmMIB=snmpUsmMIB, usmMIBObjects=usmMIBObjects, usmStats=usmStats, usmStatsUnsupportedSecLevels=usmStatsUnsupportedSecLevels, usmStatsNotInTimeWindows=usmStatsNotInTimeWindows, usmStatsUnknownUserNames=usmStatsUnknownUserNames, usmStatsUnknownEngineIDs=usmStatsUnknownEngineIDs, usmStatsWrongDigests=usmStatsWrongDigests, usmStatsDecryptionErrors=usmStatsDecryptionErrors, usmUser=usmUser, usmUserSpinLock=usmUserSpinLock, usmUserTable=usmUserTable, usmUserEntry=usmUserEntry, usmUserEngineID=usmUserEngineID, usmUserName=usmUserName, usmUserSecurityName=usmUserSecurityName, usmUserCloneFrom=usmUserCloneFrom, usmUserAuthProtocol=usmUserAuthProtocol, usmUserAuthKeyChange=usmUserAuthKeyChange, usmUserOwnAuthKeyChange=usmUserOwnAuthKeyChange, usmUserPrivProtocol=usmUserPrivProtocol, usmUserPrivKeyChange=usmUserPrivKeyChange, usmUserOwnPrivKeyChange=usmUserOwnPrivKeyChange, usmUserPublic=usmUserPublic, usmUserStorageType=usmUserStorageType, usmUserStatus=usmUserStatus, usmMIBConformance=usmMIBConformance, usmMIBCompliances=usmMIBCompliances, usmMIBGroups=usmMIBGroups)

# Groups
mibBuilder.exportSymbols("SNMP-USER-BASED-SM-MIB", usmMIBBasicGroup=usmMIBBasicGroup)

# Compliances
mibBuilder.exportSymbols("SNMP-USER-BASED-SM-MIB", usmMIBCompliance=usmMIBCompliance)
