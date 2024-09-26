# Flyte-Console-support-MsgPack

## Javscript Version
npm: 10.7.0
Node.js: v18.20.4

## Python Version
python: 3.12.4 
flytekit branch: https://github.com/flyteorg/flytekit/pull/2760

## Golang Version
go: 1.22.0 darwin/arm64
flyte branch: https://github.com/flyteorg/flyte/pull/5776


## Show on Flyte Console

### Python to JavaScript
```python
python generate_msgpack_bytes.py 
```

```javascript
/Users/future-outlier/.nvm/versions/node/v18.20.4/bin/node /Users/future-outlier/code/dev/build/PR/JSON/Flyte-Console-support-MsgPack/python_to_javascript.js
Decoded Data:
{
  a: -1,
  b: 2.1,
  c: 'Hello, Flyte',
  d: false,
  e: [ 0, 1, 2, -1, -2 ],
  f: [ { path: 's3://my-s3-bucket/example.txt' } ],
  g: [ [ 0 ], [ 1 ], [ -1 ] ],
  h: [
    Map(1) { 0 => false },
    Map(1) { 1 => true },
    Map(1) { -1 => true }
  ],
  i: Map(3) { 0 => false, 1 => true, -1 => false },
  j: Map(3) {
    0 => { path: 's3://my-s3-bucket/example.txt' },
    1 => { path: 's3://my-s3-bucket/example.txt' },
    -1 => { path: 's3://my-s3-bucket/example.txt' }
  },
  k: Map(1) { 0 => [ 0, 1, -1 ] },
  l: Map(1) { 1 => Map(1) { -1 => 0 } },
  m: { key: 'value' },
  n: { path: 's3://my-s3-bucket/example.txt' },
  o: { path: 's3://my-s3-bucket/s3_flyte_dir' },
  inner_dc: {
    a: -1,
    b: 2.1,
    c: 'Hello, Flyte',
    d: false,
    e: [ 0, 1, 2, -1, -2 ],
    f: [ [Object] ],
    g: [ [Array], [Array], [Array] ],
    h: [ [Map], [Map], [Map] ],
    i: Map(3) { 0 => false, 1 => true, -1 => false },
    j: Map(3) { 0 => [Object], 1 => [Object], -1 => [Object] },
    k: Map(1) { 0 => [Array] },
    l: Map(1) { 1 => [Map] },
    m: { key: 'value' },
    n: { path: 's3://my-s3-bucket/example.txt' },
    o: { path: 's3://my-s3-bucket/s3_flyte_dir' },
    enum_status: 'pending'
  },
  enum_status: 'pending'
}



```

### Golang to JavaScript
golang: https://github.com/flyteorg/flyte/pull/5776/files#diff-ee7f936e440a7e043b3bc7acb4ea255ba991dea8f3144d24ab276c3a292de018R96-R111
Run a workflow with single binary.

```javascript
/Users/future-outlier/.nvm/versions/node/v18.20.4/bin/node /Users/future-outlier/code/dev/build/PR/JSON/Flyte-Console-support-MsgPack/golang_to_javascript.js
Decoded Data: {
  a: -1,
  b: 3.14,
  c: 'Hello, Flyte',
  d: false,
  e: [ 0, 1, 2, -1, -2 ],
  f: [ { path: 's3://my-s3-bucket/example.txt' } ],
  g: [ [ 0 ], [ 1 ], [ -1 ] ],
  h: [
    Map(1) { 0 => false },
    Map(1) { 1 => true },
    Map(1) { -1 => true }
  ],
  i: Map(3) { 0 => false, 1 => true, -1 => false },
  j: Map(3) {
    0 => { path: 's3://my-s3-bucket/example.txt' },
    1 => { path: 's3://my-s3-bucket/example.txt' },
    -1 => { path: 's3://my-s3-bucket/example.txt' }
  },
  k: Map(1) { 0 => [ 0, 1, -1 ] },
  l: Map(1) { 1 => Map(1) { -1 => 0 } },
  m: { key: 'value' },
  n: { path: 's3://my-s3-bucket/example.txt' },
  o: { path: 's3://my-s3-bucket/s3_flyte_dir' },
  inner_dc: {
    a: -1,
    b: 2.1,
    c: 'Hello, Flyte',
    d: false,
    e: [ 0, 1, 2, -1, -2 ],
    f: [ [Object] ],
    g: [ [Array], [Array], [Array] ],
    h: [ [Map], [Map], [Map] ],
    i: Map(3) { 0 => false, 1 => true, -1 => false },
    j: Map(3) { 0 => [Object], 1 => [Object], -1 => [Object] },
    k: Map(1) { 0 => [Array] },
    l: Map(1) { 1 => [Map] },
    m: { key: 'value' },
    n: { path: 's3://my-s3-bucket/example.txt' },
    o: { path: 's3://my-s3-bucket/s3_flyte_dir' },
    enum_status: 'pending'
  },
  enum_status: 'pending'
}
```
