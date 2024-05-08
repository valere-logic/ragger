from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class getBuildIndexRequest(_message.Message):
    __slots__ = ("conversationId", "fileName")
    CONVERSATIONID_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    conversationId: str
    fileName: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, conversationId: _Optional[str] = ..., fileName: _Optional[_Iterable[str]] = ...) -> None: ...

class getBuildIndexResponse(_message.Message):
    __slots__ = ("conversationId", "fileNameList", "status")
    class IndexStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INDEXED: _ClassVar[getBuildIndexResponse.IndexStatus]
        NOT_FOUND: _ClassVar[getBuildIndexResponse.IndexStatus]
    INDEXED: getBuildIndexResponse.IndexStatus
    NOT_FOUND: getBuildIndexResponse.IndexStatus
    CONVERSATIONID_FIELD_NUMBER: _ClassVar[int]
    FILENAMELIST_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    conversationId: str
    fileNameList: _containers.RepeatedScalarFieldContainer[str]
    status: getBuildIndexResponse.IndexStatus
    def __init__(self, conversationId: _Optional[str] = ..., fileNameList: _Optional[_Iterable[str]] = ..., status: _Optional[_Union[getBuildIndexResponse.IndexStatus, str]] = ...) -> None: ...

class buildIndexRequest(_message.Message):
    __slots__ = ("conversationId", "indexAttachments", "toolName", "subQuestionId")
    class IndexAttachmentsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    CONVERSATIONID_FIELD_NUMBER: _ClassVar[int]
    INDEXATTACHMENTS_FIELD_NUMBER: _ClassVar[int]
    TOOLNAME_FIELD_NUMBER: _ClassVar[int]
    SUBQUESTIONID_FIELD_NUMBER: _ClassVar[int]
    conversationId: str
    indexAttachments: _containers.ScalarMap[str, str]
    toolName: str
    subQuestionId: str
    def __init__(self, conversationId: _Optional[str] = ..., indexAttachments: _Optional[_Mapping[str, str]] = ..., toolName: _Optional[str] = ..., subQuestionId: _Optional[str] = ...) -> None: ...

class buildIndexResponse(_message.Message):
    __slots__ = ("conversationId", "defaultVectorStore", "docStore", "graphStore", "indexStore", "status")
    class IndexStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INDEXED: _ClassVar[buildIndexResponse.IndexStatus]
        NOT_FOUND: _ClassVar[buildIndexResponse.IndexStatus]
    INDEXED: buildIndexResponse.IndexStatus
    NOT_FOUND: buildIndexResponse.IndexStatus
    CONVERSATIONID_FIELD_NUMBER: _ClassVar[int]
    DEFAULTVECTORSTORE_FIELD_NUMBER: _ClassVar[int]
    DOCSTORE_FIELD_NUMBER: _ClassVar[int]
    GRAPHSTORE_FIELD_NUMBER: _ClassVar[int]
    INDEXSTORE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    conversationId: str
    defaultVectorStore: bytes
    docStore: bytes
    graphStore: bytes
    indexStore: bytes
    status: buildIndexResponse.IndexStatus
    def __init__(self, conversationId: _Optional[str] = ..., defaultVectorStore: _Optional[bytes] = ..., docStore: _Optional[bytes] = ..., graphStore: _Optional[bytes] = ..., indexStore: _Optional[bytes] = ..., status: _Optional[_Union[buildIndexResponse.IndexStatus, str]] = ...) -> None: ...

class deleteBuildIndexRequest(_message.Message):
    __slots__ = ("conversationId", "fileName")
    CONVERSATIONID_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    conversationId: str
    fileName: str
    def __init__(self, conversationId: _Optional[str] = ..., fileName: _Optional[str] = ...) -> None: ...

class deleteBuildIndexResponse(_message.Message):
    __slots__ = ("conversationId", "fileName", "status")
    class DeletionStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DELETED: _ClassVar[deleteBuildIndexResponse.DeletionStatus]
        NOT_FOUND: _ClassVar[deleteBuildIndexResponse.DeletionStatus]
        FAILED: _ClassVar[deleteBuildIndexResponse.DeletionStatus]
    DELETED: deleteBuildIndexResponse.DeletionStatus
    NOT_FOUND: deleteBuildIndexResponse.DeletionStatus
    FAILED: deleteBuildIndexResponse.DeletionStatus
    CONVERSATIONID_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    conversationId: str
    fileName: str
    status: deleteBuildIndexResponse.DeletionStatus
    def __init__(self, conversationId: _Optional[str] = ..., fileName: _Optional[str] = ..., status: _Optional[_Union[deleteBuildIndexResponse.DeletionStatus, str]] = ...) -> None: ...
