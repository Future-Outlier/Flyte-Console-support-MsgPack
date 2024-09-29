# Flyte-Console-support-MsgPack
## Start a SandBox
```bash
flytectl demo start --image futureoutlier/flyte:msgpack-idl --force
```

## Important
Please read [here](https://github.com/flyteorg/flyte/blob/master/rfc/system/5741-binary-idl-with-message-pack.md#flyteconsole) first, then see the example to know both python and golang can convert their msgpack bytes to javascript object.

## Javscript Version
npm: 10.7.0

Node.js: v18.20.4

## Python Version
python: 3.12.4 

flytekit branch: https://github.com/flyteorg/flytekit/pull/2760

## Golang Version
go: 1.22.0 darwin/arm64
flyte branch: https://github.com/flyteorg/flyte/pull/5776

## Deployed MSGPACK Workflow on Union
[code](./union_workflow.py)

MSGPACK IDL workflow on Union: 
https://dogfood-gcp.cloud-staging.union.ai/console/projects/flytesnacks/domains/development/executions/attcxwwnjx8gcjhwpcmr/nodes

## Show on Flyte Console

### Python to JavaScript
```python
python generate_msgpack_bytes.py 
```

```javascript
/Users/future-outlier/.nvm/versions/node/v18.20.4/bin/node /Users/future-outlier/code/dev/build/PR/JSON/Flyte-Console-support-MsgPack/python_to_javascript.js
Decoded Data: {
    a: -1,
        b: 2.1,
        c: 'Hello, Flyte',
        d: false,
        e: [ 0, 1, 2, -1, -2 ],
        f: [ { path: 's3://my-s3-bucket/example.txt' } ],
        g: [ [ 0 ], [ 1 ], [ -1 ] ],
        h: [ { '0': false }, { '1': true }, { '-1': true } ],
        i: { '0': false, '1': true, '-1': false },
    j: {
        '0': { path: 's3://my-s3-bucket/example.txt' },
        '1': { path: 's3://my-s3-bucket/example.txt' },
        '-1': { path: 's3://my-s3-bucket/example.txt' }
    },
    k: { '0': [ 0, 1, -1 ] },
    l: { '1': { '-1': 0 } },
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
            h: [ [Object], [Object], [Object] ],
            i: { '0': false, '1': true, '-1': false },
        j: { '0': [Object], '1': [Object], '-1': [Object] },
        k: { '0': [Array] },
        l: { '1': [Object] },
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
        h: [ { '0': false }, { '1': true }, { '-1': true } ],
        i: { '0': false, '1': true, '-1': false },
    j: {
        '0': { path: 's3://my-s3-bucket/example.txt' },
        '1': { path: 's3://my-s3-bucket/example.txt' },
        '-1': { path: 's3://my-s3-bucket/example.txt' }
    },
    k: { '0': [ 0, 1, -1 ] },
    l: { '1': { '-1': 0 } },
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
            h: [ [Object], [Object], [Object] ],
            i: { '0': false, '1': true, '-1': false },
        j: { '0': [Object], '1': [Object], '-1': [Object] },
        k: { '0': [Array] },
        l: { '1': [Object] },
        m: { key: 'value' },
        n: { path: 's3://my-s3-bucket/example.txt' },
        o: { path: 's3://my-s3-bucket/s3_flyte_dir' },
        enum_status: 'pending'
    },
    enum_status: 'pending'
}
```
