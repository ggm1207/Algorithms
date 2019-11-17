import json
from pprint import pprint
from blockinfo import blockinfo
from collections import defaultdict

# 트랜잭션에서 모든 입력의 합은 모든 출력의 합보다 크거나 같아야합니다. 입력 값이 출력값을 초과 할 경우, 
# 그 차액은 거래 수수료 로 간주 되며, 거래를 먼저 블록 체인에 포함한 사람이 상환 할 수 있습니다.

if __name__ == "__main__":
    # print(blockinfo)
    # json.loads(blockinfo)
    # print(blockinfo.keys())
    input_value = 0
    output_value = 0
    iv, ov = 0, 0
    for block in blockinfo['tx']:
        key_list = block.keys()
        a, b = 0, 0
        if 'inputs' in key_list:
            for inputs in block['inputs']:
                input_keys = inputs.keys() # sequence or prev_out
                if 'prev_out' in input_keys:
                    prev_keys = inputs['prev_out'].keys()
                    if 'value' in prev_keys:
                        a += inputs['prev_out']['value']
        if 'out' in key_list:
            for outs in block['out']:
                outs_keys = outs.keys()
                if 'value' in outs_keys:
                    b += outs['value']
        

        if min(a,b) == 0:
            continue
        input_value += a
        output_value += b
    
    
    
    print(iv, ov)

    print(input_value)
    print(output_value)
    print(input_value - output_value)
    if input_value < output_value:
        print(0)
    else:
        print(input_value - output_value)
 
    # pprint(blockinfo)
    