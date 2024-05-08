from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class getAnswerCitationsRequest(_message.Message):
    __slots__ = ("conversationId", "subQuestion", "params", "toolName", "subQuestionId")
    CONVERSATIONID_FIELD_NUMBER: _ClassVar[int]
    SUBQUESTION_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    TOOLNAME_FIELD_NUMBER: _ClassVar[int]
    SUBQUESTIONID_FIELD_NUMBER: _ClassVar[int]
    conversationId: str
    subQuestion: str
    params: SubParams
    toolName: str
    subQuestionId: str
    def __init__(self, conversationId: _Optional[str] = ..., subQuestion: _Optional[str] = ..., params: _Optional[_Union[SubParams, _Mapping]] = ..., toolName: _Optional[str] = ..., subQuestionId: _Optional[str] = ...) -> None: ...

class getAnswerCitationsResponse(_message.Message):
    __slots__ = ("Answer", "citations", "status")
    ANSWER_FIELD_NUMBER: _ClassVar[int]
    CITATIONS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    Answer: str
    citations: _containers.RepeatedCompositeFieldContainer[SubConvCitation]
    status: str
    def __init__(self, Answer: _Optional[str] = ..., citations: _Optional[_Iterable[_Union[SubConvCitation, _Mapping]]] = ..., status: _Optional[str] = ...) -> None: ...

class SubConvCitation(_message.Message):
    __slots__ = ("filename", "pagenum", "document_id", "text", "node")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    PAGENUM_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_ID_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    NODE_FIELD_NUMBER: _ClassVar[int]
    filename: str
    pagenum: int
    document_id: str
    text: str
    node: bytes
    def __init__(self, filename: _Optional[str] = ..., pagenum: _Optional[int] = ..., document_id: _Optional[str] = ..., text: _Optional[str] = ..., node: _Optional[bytes] = ...) -> None: ...

class SubEmpty(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SubParams(_message.Message):
    __slots__ = ("qe_k", "qe_top_k", "qe_temperature", "qe_max_new_tokens", "qe_score_threshold", "qe_repetition_penalty", "qe_reranker_top_n", "qe_similarity_top_k")
    QE_K_FIELD_NUMBER: _ClassVar[int]
    QE_TOP_K_FIELD_NUMBER: _ClassVar[int]
    QE_TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    QE_MAX_NEW_TOKENS_FIELD_NUMBER: _ClassVar[int]
    QE_SCORE_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    QE_REPETITION_PENALTY_FIELD_NUMBER: _ClassVar[int]
    QE_RERANKER_TOP_N_FIELD_NUMBER: _ClassVar[int]
    QE_SIMILARITY_TOP_K_FIELD_NUMBER: _ClassVar[int]
    qe_k: int
    qe_top_k: int
    qe_temperature: float
    qe_max_new_tokens: int
    qe_score_threshold: float
    qe_repetition_penalty: float
    qe_reranker_top_n: int
    qe_similarity_top_k: int
    def __init__(self, qe_k: _Optional[int] = ..., qe_top_k: _Optional[int] = ..., qe_temperature: _Optional[float] = ..., qe_max_new_tokens: _Optional[int] = ..., qe_score_threshold: _Optional[float] = ..., qe_repetition_penalty: _Optional[float] = ..., qe_reranker_top_n: _Optional[int] = ..., qe_similarity_top_k: _Optional[int] = ...) -> None: ...

class SubLengthRequest(_message.Message):
    __slots__ = ("text",)
    TEXT_FIELD_NUMBER: _ClassVar[int]
    text: str
    def __init__(self, text: _Optional[str] = ...) -> None: ...

class SubLengthResponse(_message.Message):
    __slots__ = ("length",)
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    length: int
    def __init__(self, length: _Optional[int] = ...) -> None: ...

class SubModelContextLengthResponse(_message.Message):
    __slots__ = ("contextLength",)
    CONTEXTLENGTH_FIELD_NUMBER: _ClassVar[int]
    contextLength: int
    def __init__(self, contextLength: _Optional[int] = ...) -> None: ...
