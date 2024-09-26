import typing
import os
from dataclasses import dataclass, fields, field
from typing import Dict, List
from flytekit.types.file import FlyteFile
from flytekit.types.directory import FlyteDirectory
from flytekit.models.literals import StructuredDataset
from flytekit.types.schema import FlyteSchema

from mashumaro.mixins.json import DataClassJSONMixin
from flytekit import task, workflow, ImageSpec
from dataclasses_json import dataclass_json
import datetime
from enum import Enum
from mashumaro.codecs.msgpack import MessagePackDecoder, MessagePackEncoder


flytekit_hash = "f50b1eeaa9040d548f5a94e7d2580cdbf20afc37"
flytekit = f"git+https://github.com/flyteorg/flytekit.git@{flytekit_hash}"
image = ImageSpec(
    packages=[flytekit],
    apt_packages=["git"],
    registry="localhost:30000",
)

# image = "futureoutlier/flytekit:msg-idl-1237"

class Status(Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"

@dataclass
# class InnerDC(DataClassJSONMixin):
class InnerDC:
    a: int = -1
    b: float = 2.1
    c: str = "Hello, Flyte"
    d: bool = False
    e: List[int] = field(default_factory=lambda: [0, 1, 2, -1, -2])
    f: List[FlyteFile] = field(default_factory=lambda: [FlyteFile("s3://my-s3-bucket/example.txt"),])
    g: List[List[int]] = field(default_factory=lambda: [[0], [1], [-1]])
    h: List[Dict[int, bool]] = field(default_factory=lambda: [{0: False}, {1: True}, {-1: True}])
    i: Dict[int, bool] = field(default_factory=lambda: {0: False, 1: True, -1: False})
    j: Dict[int, FlyteFile] = field(default_factory=lambda: {0: FlyteFile("s3://my-s3-bucket/example.txt"),
                                                             1: FlyteFile("s3://my-s3-bucket/example.txt"),
                                                             -1: FlyteFile("s3://my-s3-bucket/example.txt")})
    k: Dict[int, List[int]] = field(default_factory=lambda: {0: [0, 1, -1]})
    l: Dict[int, Dict[int, int]] = field(default_factory=lambda: {1: {-1: 0}})
    m: dict = field(default_factory=lambda: {"key": "value"})
    n: FlyteFile = field(default_factory=lambda: FlyteFile("s3://my-s3-bucket/example.txt"))
    o: FlyteDirectory = field(default_factory=lambda: FlyteDirectory("s3://my-s3-bucket/s3_flyte_dir"))
    enum_status: Status = field(default=Status.PENDING)

@dataclass
# class DC(DataClassJSONMixin):
class DC:
    a: int = -1
    b: float = 2.1
    c: str = "Hello, Flyte"
    d: bool = False
    e: List[int] = field(default_factory=lambda: [0, 1, 2, -1, -2])
    f: List[FlyteFile] = field(default_factory=lambda: [FlyteFile("s3://my-s3-bucket/example.txt"), ])
    g: List[List[int]] = field(default_factory=lambda: [[0], [1], [-1]])
    h: List[Dict[int, bool]] = field(default_factory=lambda: [{0: False}, {1: True}, {-1: True}])
    i: Dict[int, bool] = field(default_factory=lambda: {0: False, 1: True, -1: False})
    j: Dict[int, FlyteFile] = field(default_factory=lambda: {0: FlyteFile("s3://my-s3-bucket/example.txt"),
                                                             1: FlyteFile("s3://my-s3-bucket/example.txt"),
                                                             -1: FlyteFile("s3://my-s3-bucket/example.txt")})
    k: Dict[int, List[int]] = field(default_factory=lambda: {0: [0, 1, -1]})
    l: Dict[int, Dict[int, int]] = field(default_factory=lambda: {1: {-1: 0}})
    m: dict = field(default_factory=lambda: {"key": "value"})
    n: FlyteFile = field(default_factory=lambda: FlyteFile("s3://my-s3-bucket/example.txt"))
    o: FlyteDirectory = field(default_factory=lambda: FlyteDirectory("s3://my-s3-bucket/s3_flyte_dir"))
    inner_dc: InnerDC = field(default_factory=lambda: InnerDC())
    enum_status: Status = field(default=Status.PENDING)

python_val = DC()
msgpack_bytes = MessagePackEncoder(DC).encode(python_val)
# Write the bytes to a file
with open("./python_msgpack_bytes", "wb") as f:
    f.write(msgpack_bytes)

print("MsgPack bytes written to ./python_msgpack_bytes")

