#!/bin/python3
try:
    import argparse
    import ast
    import builtins as __builtins__
    import re
    import random
    import sys
    import zlib
    import base64
    import bz2
    import marshal
    import colorama
    colorama.init()
    from datetime import datetime
    import pytz
    import time
    import pickle
    from pystyle import Colors, Colorate, Col, System, Add
    from typing import Set, Dict, List, Tuple, Any, Union
    import sys
    System.Clear()
    print('>> Loading...', end='\r')
    VIP_ANTI = '\nif len(globals()) != 100:\n    globals()["_HOOK_CAI_LON_"]=[[[[[((\'TrinhNguyen0611\') * 987654321)] * 987654321] * 987654321] * 987654321] * 987654321] * 2123000000 * 2123000000\n    exit()\nif __import__(\'os\').environ.get("HTTP_TOOLKIT_ACTIVE") == "true":\n    globals()["_HOOK_CAI_LON_"]=[[[[[((\'TrinhNguyen0611\') * 987654321)] * 987654321] * 987654321] * 987654321] * 987654321] * 2123000000 * 2123000000\n    exit()\nfor ev in ["SSL_CERT_FILE", "NODE_EXTRA_CA_CERTS", "PATH"]:\n    if ev in __import__(\'os\').environ and "httptoolkit" in __import__(\'os\').environ[ev].lower():\n        globals()["_HOOK_CAI_LON_"]=[[[[[((\'TrinhNguyen0611\') * 987654321)] * 987654321] * 987654321] * 987654321] * 987654321] * 2123000000 * 2123000000\n        exit()\nfor px in ["HTTP_PROXY", "HTTPS_PROXY", "http_proxy", "https_proxy"]:\n    if px in __import__(\'os\').environ and "127.0.0.1:8000" in __import__(\'os\').environ[px]:\n        globals()["_HOOK_CAI_LON_"]=[[[[[((\'TrinhNguyen0611\') * 987654321)] * 987654321] * 987654321] * 987654321] * 987654321] * 2123000000 * 2123000000\n        exit()\ntry:\n    h = requests.get("https://example.com", timeout=5).headers\n    if any("HTTP-Toolkit" in h.get(x, "") for x in ["Server", "Via", "X-Powered-By"]):\n        globals()["_HOOK_CAI_LON_"]=[[[[[((\'TrinhNguyen0611\') * 987654321)] * 987654321] * 987654321] * 987654321] * 987654321] * 2123000000 * 2123000000\n        exit()\nexcept:\n    pass\n'
    dark = Col.white
    light = Col.light_gray
    sakura_ = Colors.StaticMIX((Col.red, Col.purple))
    bsakura_ = Colors.StaticMIX((Col.red, Col.purple, Col.purple))
    sakura = '\n    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣧⣼⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀\n    ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀\n    ⠀⠀⠀⢀⣀⣀⣀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⣀⣀⣀⡀⠀⠀⠀\n    ⠀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⠀  Code By NguyenXuanTrinh (Aka Calce)\n    ⠀⣙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣋⠀  Facebook: @Developer.NXT.IT\n    ⣿⣿⣿⣿⣿⣿⣿⠁⠀⠈⠻⠿⠀⠀⠿⠟⠁⠀⠈⣿⣿⣿⣿⣿⣿⣿  Telegram: @CalceIsMe\n    ⠘⢿⣿⣿⣿⣿⣿⣦⣤⣤⣄⡀⠀⠀⢀⣠⣤⣤⣴⣿⣿⣿⣿⣿⡿⠃  OBF-Bot: @TrinhNguyen0611_bot\n    ⠀⠀⠙⢿⣿⣿⣿⣿⣿⠿⠋⠀⣠⣄⠀⠙⠿⣿⣿⣿⣿⣿⡿⠋⠀⠀\n    ⠀⠀⠀⢰⣿⣿⣿⣿⣿⠀⠀⢠⣿⣿⡄⠀⠀⣿⣿⣿⣿⣿⡆⠀⠀⠀\n    ⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀\n    ⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀\n    ⠀⠀⠀⠈⠛⠛⣿⣿⣿⣿⣿⡿⠛⠛⢿⣿⣿⣿⣿⣿⠛⠛⠁⠀⠀⠀\n    ⠀⠀⠀⠀⠀⠀⠘⠛⠛⠉⠁⠀⠀⠀⠀⠈⠉⠛⠛⠃⠀⠀⠀⠀⠀⠀\n'
    banner = '\n   ▄▄▄▄▄   ██   █  █▀  ▄   █▄▄▄▄ ██   \n  █     ▀▄ █ █  █▄█     █  █  ▄▀ █ █  \n▄  ▀▀▀▀▄   █▄▄█ █▀▄  █   █ █▀▀▌  █▄▄█ \n ▀▄▄▄▄▀    █  █ █  █ █   █ █  █  █  █ \n              █   █  █▄ ▄█   █      █ \n             █   ▀    ▀▀▀   ▀      █  \n            ▀                     ▀   \n'

    def p(text):
        return print(stage(text))

    def stage(text: str, symbol: str='...', col1=light, col2=None) -> str:
        if col2 is None:
            col2 = light if symbol == '...' else dark
        return f' {Col.Symbol(symbol, col1, dark)} {col2}{text}{Col.reset}'
    hcm_tz = pytz.timezone('Asia/Ho_Chi_Minh')
    current_time_hcm = datetime.now(hcm_tz)
    check_pyver = lambda a='.'.join(__import__('sys').version.split(' ')[0].split('.')[:-1]): f'''\nif ".".join(__TrinhNguyen0611__[{Pycloak().encode('__import__')}]({Pycloak().encode('sys')}).version.split(" ")[0].split(".")[:-1]) != "{a}":\n    print("\\n >> Your Python is {'.'.join(__import__('sys').version.split(' ')[0].split('.')[:-1])}\\n You need to run this code in Python {a}\\n Using Python other than {a} won't work!\\n")\n    input('Press Enter to Exit! ')\n    exit(-1)\n[print(c, end="", flush=True) or __TrinhNguyen0611__[{Pycloak().encode('__import__')}]({Pycloak().encode('time')}).sleep(0.01) for c in ">> Loading... <<"]\n'''
    anti = '\n'
    global pro
    global anti_debug
    global ANTI_PYCDC
    _float = '_Trinh2k10_'
    _int = '_Trinh2010_'
    _str = '_TrinhKhongBeDe_'
    _bool = '_TrinhCuTo_'
    _bytes = '_TrinhHocCode_'
    __print = 'lambdaᅠ'
    __input = 'execᅠ'
    _eval = '_TrinhCodeHoiNgu_'
    __ALIASES__ = {}
    __DECLARED_NAMES__ = set()
    __MODULE_NAMES__ = set()
    hard_code = '\n'
    list_ten_bien = ['TrinhSieuDepTrai', 'CalceSieuCapVip', 'TrinhCodeThuongThua', 'CalceVoDichTheGioi', 'TrinhChuyenGiaPro', 'CalceBacThoDinhCao', 'TrinhCongNgheDinh', 'CalceLapTrinhMaster', 'TrinhSangTaoVoSong', 'CalceVuongGiaCode', 'TrinhThuatToanHay', 'CalceHackerPro', 'TrinhThanhCongLon', 'CalceToiThuongDev', 'TrinhAnDanhElite', 'CalceChienThanCode', 'TrinhProMaxVIP', 'CalceTruyenKyLapTrinh', 'TrinhMasterMind', 'CalceUltimateDev', 'TrinhDevKing', 'CalceInfinityCode', 'TrinhCodeWarrior', 'CalceChampionCoder', 'TrinhCyberHero', 'CalceTheBestDev', 'TrinhAIWizard', 'CalceOverlordCoder', 'TrinhEliteHacker', 'CalceDarkMode', 'TrinhQuantumTech', 'CalceGodLike']

    def varsobf(v):
        return f"('DitConBaGiaMay') if 2010 < 611 or 611 > 2010 or 12345 > 67890 or 98765 < 54321 or 'test' == 'false' or 0 == 1 or False == True or 1 == 2 or 10 > 20 or {random.randint(1, 1000)} > {random.randint(101, 20000000000)} else {v}"

    def spam_hanzi():
        hanzi_chars = '天地玄黄宇宙洪荒日月盈昃辰宿列张'
        return f'__{random.randint(100000000, 10000000000)}{''.join(random.choices(hanzi_chars, k=10))}{random.randint(100000000, 100000000000)}__'

    def obf_gl(input_string):
        return ''.join([chr((ord(c) - (65 if c.isupper() else 97) + 10) % 26 + (65 if c.isupper() else 97)) if c.isalpha() else c for c in input_string])

    def build_anti_pycdc():
        antipycdc = ''
        e = {'Z': '1/0,', 'T': 'len+1,', 'N': 'xyz,', 'T2': '"a"+1,', 'I': '[][99],', 'K': '{}[""],', 'M': "__import__('xyz'),", 'V': 'int("a",99),', 'A': '[].__x,', 'F': 'open("ww"),'}
        for k in e:
            e[k] = e[k] * 1000
        antipycdc += '\n'.join((f'try:({v})\nexcept:0\n' for v in e.values()))
        globals()['ANTI_PYCDC'] = f'\ntry:pass\nexcept:pass\nelse:pass\nfinally:pass\n{antipycdc}\nfinally:int(2010-611)\n'

    def build_var():
        global anti_debug, pro
        concacto = open('anti.py', 'r', encoding='utf-8-sig').read()
        globals()['anti_debug'] = 'open(__file__, "w", encoding="utf-8").write("Địt Con Bà Mày Dec Hook Cái Lồn!") if (len(open(__file__, "r", encoding="utf-8").read().split("\\n"))) != 51 else None\n' + concacto + '\n'
        pro = ANTI_PYCDC
        list_ten_bienn = ['TrinhSieuDepTrai', 'CalceSieuCapVip', 'TrinhCodeThuongThua', 'CalceVoDichTheGioi', 'TrinhChuyenGiaPro', 'CalceBacThoDinhCao', 'TrinhCongNgheDinh', 'CalceLapTrinhMaster', 'TrinhSangTaoVoSong', 'CalceVuongGiaCode', 'TrinhThuatToanHay', 'CalceHackerPro', 'TrinhThanhCongLon', 'CalceToiThuongDev', 'TrinhAnDanhElite', 'CalceChienThanCode', 'TrinhProMaxVIP', 'CalceTruyenKyLapTrinh', 'TrinhMasterMind', 'CalceUltimateDev', 'TrinhDevKing', 'CalceInfinityCode', 'TrinhCodeWarrior', 'CalceChampionCoder', 'TrinhCyberHero', 'CalceTheBestDev', 'TrinhAIWizard', 'CalceOverlordCoder', 'TrinhEliteHacker', 'CalceDarkMode', 'TrinhQuantumTech', 'CalceGodLike']
        Hehe = [f'{_bool} = {varsobf('bool')}', f'{_str} = {varsobf('str')}', f'{_int} = {varsobf('int')}', f'{_float} = {varsobf('float')}', f'{_bytes} = {varsobf('bytes')}', f'{_eval} = {varsobf('eval')}', f'{__print} = {varsobf('print')}', f'{__input} = {varsobf('input')}']
        while list_ten_bienn:
            i = random.choice(list_ten_bienn)
            hhh = random.randint(1, 10)
            if hhh == 1:
                pro += f'''globals()[''.join([chr(((ord(c) - (65 if c.isupper() else 97) - 10) % 26) + (65 if c.isupper() else 97)) if c.isalpha() else c for c in "{obf_gl(i)}"])] = lambda concacmemaybeolam, jackbocon, meomeo, bucuanhdi: (\n            concacmemaybeolam.join([chr((DIT_ME_MAY - jackbocon) // meomeo) for DIT_ME_MAY in bucuanhdi])\n            if concacmemaybeolam not in ["DitConBaMay", "TrinhObfuscate", "NguyenXuanTrinh"]\n            else (b"" if concacmemaybeolam == "TrinhObfuscate" \n                else r"" if concacmemaybeolam == "DitConBaMay" \n                else "").join([chr((DIT_ME_MAY - jackbocon) // meomeo) for DIT_ME_MAY in bucuanhdi]))\n'''
                list_ten_bienn.remove(i)
            else:
                pro += f'''globals()[''.join([chr(((ord(c) - (65 if c.isupper() else 97) - 10) % 26) + (65 if c.isupper() else 97)) if c.isalpha() else c for c in "{obf_gl(str('TrinhDitMeMay'))}"])] = lambda concacmemaybeolam, jackbocon, meomeo, bucuanhdi: (\n            concacmemaybeolam.join([chr((DIT_ME_MAY - jackbocon) // meomeo) for DIT_ME_MAY in bucuanhdi])\n            if concacmemaybeolam not in ["DitConBaMay", "TrinhObfuscate", "NguyenXuanTrinh"]\n            else (b"" if concacmemaybeolam == "TrinhObfuscate" \n                else r"" if concacmemaybeolam == "DitConBaMay" \n                else "").join([chr((DIT_ME_MAY - jackbocon) // meomeo) for DIT_ME_MAY in bucuanhdi]))\n'''
                if Hehe:
                    hello = random.choice(Hehe)
                    pro += hello + '\n'
                    Hehe.remove(hello)
            if Hehe:
                hello = random.choice(Hehe)
                pro += hello + '\n'
                Hehe.remove(hello)

    class Ast_obf:

        def rn_func(self, node, ol, nn):
            for i in ast.walk(node):
                if isinstance(i, ast.FunctionDef) and i.name == ol:
                    i.name = nn
                elif isinstance(i, ast.Attribute) and isinstance(i.value, ast.Name) and (i.value.id == ol):
                    i.value.id = nn
                elif isinstance(i, ast.Call) and isinstance(i.func, ast.Name) and (i.func.id == ol):
                    i.func.id = nn
                elif isinstance(i, ast.Name) and i.id == ol:
                    i.id = nn
            return node

        def spam(self, code):
            tree = ast.parse(code)

            def junk(en, max_value):
                cases = []
                line = max_value + 1
                for i in range(random.randint(1, 5)):
                    case_name = 'BuConCacTaoDi' + str(random.randint(2061584302080, 8658654068736))
                    case_body = [ast.If(test=ast.Compare(left=ast.Subscript(value=ast.Attribute(value=ast.Name(id=en), attr='args'), slice=ast.Constant(value=0)), ops=[ast.Eq()], comparators=[ast.Constant(value=line)]), body=[ast.Assign(targets=[ast.Name(id=case_name)], value=ast.Constant(value=random.randint(1048575, 281474976710655)), lineno=None)], orelse=[])]
                    cases.extend(case_body)
                    line += 1
                return cases

            def bl(body):
                var = 'NhinCaiLon' + str(random.randint(2061584302080, 8658654068736))
                en = 'NhinConCac' + str(random.randint(2061584302080, 8658654068736))
                tb = [ast.AugAssign(target=ast.Name(id=var), op=ast.Add(), value=ast.Constant(value=1)), ast.Try(body=[ast.Raise(exc=ast.Call(func=ast.Name(id='MemoryError'), args=[ast.Name(id=var)], keywords=[]))], handlers=[ast.ExceptHandler(type=ast.Name(id='MemoryError'), name=en, body=[])], orelse=[], finalbody=[])]
                for i in body:
                    tb[1].handlers[0].body.append(ast.If(test=ast.Compare(left=ast.Subscript(value=ast.Attribute(value=ast.Name(id=en), attr='args'), slice=ast.Constant(value=0)), ops=[ast.Eq()], comparators=[ast.Constant(value=1)]), body=[i], orelse=[]))
                tb[1].handlers[0].body.extend(junk(en, len(body) + 1))
                node = ast.Assign(targets=[ast.Name(id=var)], value=ast.Constant(value=0), lineno=None)
                return [node] + tb

            def _bl(node):
                olb = node.body
                var = '__' + str(random.randint(2061584302080, 8658654068736)) + '__'
                en = '__' + str(random.randint(2061584302080, 8658654068736)) + '__'
                tb = [ast.AugAssign(target=ast.Name(id=var), op=ast.Add(), value=ast.Constant(value=1)), ast.Try(body=[ast.Raise(exc=ast.Call(func=ast.Name(id='MemoryError'), args=[ast.Name(id=var)], keywords=[]))], handlers=[ast.ExceptHandler(type=ast.Name(id='MemoryError'), name=en, body=[])], orelse=[], finalbody=[])]
                for i in olb:
                    tb[1].handlers[0].body.append(ast.If(test=ast.Compare(left=ast.Subscript(value=ast.Attribute(value=ast.Name(id=en), attr='args'), slice=ast.Constant(value=0)), ops=[ast.Eq()], comparators=[ast.Constant(value=1)]), body=[i], orelse=[]))
                tb[1].handlers[0].body.extend(junk(en, len(olb) + 1))
                node.body = [ast.Assign(targets=[ast.Name(id=var)], value=ast.Constant(value=0), lineno=None)] + tb
                return node

            def on(node):
                """
            Process a top-level node in the AST.
            
            Args:
                node: An AST node (function or class definition)
                
            Returns:
                The processed node
            """
                if isinstance(node, ast.FunctionDef):
                    return _bl(node)
                elif isinstance(node, ast.ClassDef):
                    node.body = yuamikami_inner(node)
                    return node
                return node

            def yuamikami_inner(parent_node):
                """
            Process all nodes inside a class definition.
            
            Args:
                parent_node: A ClassDef node whose body needs to be processed
                
            Returns:
                A list of processed nodes
            """
                nb = []
                for node in parent_node.body:
                    if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                        nb.append(_bl(node))
                    elif isinstance(node, ast.ClassDef):
                        node.body = yuamikami_inner(node)
                        nb.append(node)
                    elif isinstance(node, (ast.Assign, ast.AugAssign, ast.AnnAssign)):
                        nb.extend(bl([node]))
                    elif isinstance(node, ast.Expr):
                        nb.extend(bl([node]))
                    elif isinstance(node, ast.Try):
                        node.body = process_block(node.body)
                        for handler in node.handlers:
                            handler.body = process_block(handler.body)
                        if node.orelse:
                            node.orelse = process_block(node.orelse)
                        if node.finalbody:
                            node.finalbody = process_block(node.finalbody)
                        nb.append(node)
                    else:
                        nb.append(node)
                return nb

            def process_block(block):
                """
            Process a block of code (used for try/except/else/finally blocks).
            
            Args:
                block: A list of AST nodes to process
                
            Returns:
                A list of processed nodes
            """
                nb = []
                for node in block:
                    if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                        nb.append(_bl(node))
                    elif isinstance(node, ast.ClassDef):
                        node.body = yuamikami_inner(node)
                        nb.append(node)
                    elif isinstance(node, (ast.Assign, ast.AugAssign, ast.AnnAssign)):
                        nb.extend(bl([node]))
                    elif isinstance(node, ast.Expr):
                        nb.extend(bl([node]))
                    elif isinstance(node, ast.Try):
                        node.body = process_block(node.body)
                        for handler in node.handlers:
                            handler.body = process_block(handler.body)
                        if node.orelse:
                            node.orelse = process_block(node.orelse)
                        if node.finalbody:
                            node.finalbody = process_block(node.finalbody)
                        nb.append(node)
                    else:
                        nb.append(node)
                return nb

            def yuamikami(tree):
                """
            Process the entire AST.
            
            Args:
                tree: The AST module node
                
            Returns:
                A list of processed nodes for the module body
            """
                nb = []
                for node in tree.body:
                    if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                        nb.append(on(node))
                    elif isinstance(node, (ast.Assign, ast.AugAssign, ast.AnnAssign)):
                        nb.extend(bl([node]))
                    elif isinstance(node, ast.Expr):
                        nb.extend(bl([node]))
                    elif isinstance(node, ast.Try):
                        node.body = process_block(node.body)
                        for handler in node.handlers:
                            handler.body = process_block(handler.body)
                        if node.orelse:
                            node.orelse = process_block(node.orelse)
                        if node.finalbody:
                            node.finalbody = process_block(node.finalbody)
                        nb.append(node)
                    else:
                        nb.append(node)
                return nb
            nb = yuamikami(tree)
            tree.body = nb
            return tree

        def obfct(self, string: str, string_type: str='') -> ast.AST:
            try:
                if string == '':
                    return ast.Constant(value='')
                dep_trai = random.choice(list_ten_bien)
                encoded = [ord(c) * 611 + 2010 for c in string]
                jackbocon = 2010
                meomeo = 611
                if string_type == 'r':
                    return ast.parse(f"{_str}((lambda: {dep_trai}('DitConBaMay', {jackbocon}, {meomeo}, {encoded}))())").body[0].value
                else:
                    return ast.parse(f"{_str}((lambda: {dep_trai}('NguyenXuanTrinh', {jackbocon}, {meomeo}, {encoded}))())").body[0].value
            except Exception as e:
                print(f'Error occurred in obfct: {str(e)}')
                return ast.Constant(value=string)

        def random_match_case(self):
            var1 = ast.Constant(value=spam_hanzi(), kind=None)
            var2 = ast.Constant(value=spam_hanzi(), kind=None)
            return ast.Match(subject=ast.Compare(left=var1, ops=[ast.Eq()], comparators=[var2]), cases=[ast.match_case(pattern=ast.MatchValue(value=ast.Constant(value=True, kind=None)), body=[ast.Assign(lineno=0, col_offset=0, targets=[], value=ast.Raise(exc=ast.Call(func=ast.Name(id='MemoryError', ctx=ast.Load()), args=[], keywords=[ast.Constant(value=True, kind=None)])))]), ast.match_case(pattern=ast.MatchValue(value=ast.Constant(value=True, kind=None)), body=[ast.Assign(lineno=0, col_offset=0, targets=[ast.Name(id='_' + spam_hanzi(), ctx=ast.Store())], value=ast.Constant(value=[True, False], kind=None)), ast.Expr(lineno=0, col_offset=0, value=ast.Call(func=ast.Name(id=_str, ctx=ast.Load()), args=[ast.Constant(value='_' + spam_hanzi(), kind=None)], keywords=[]))])])

        def trycatch(self, body, loop):
            """
        Wraps each element in body with nested try-except blocks based on loop count.
        Each try block contains a random match-case statement and raises a MemoryError.
        
        Args:
            body: List of AST nodes to wrap in try-except blocks
            loop: Number of nested try-except blocks to create
            
        Returns:
            List of AST nodes wrapped in try-except blocks
        """
            result_nodes = []
            for x in body:
                current_node = x
                for _ in range(loop):
                    try_block = ast.Try(body=[self.random_match_case(), ast.Raise(exc=ast.Call(func=ast.Name(id='MemoryError', ctx=ast.Load()), args=[], keywords=[]), cause=None)], handlers=[ast.ExceptHandler(type=ast.Name(id='MemoryError', ctx=ast.Load()), name='_' + spam_hanzi(), body=[current_node])], orelse=[], finalbody=[])
                    current_node = try_block
                result_nodes.append(current_node)
            return result_nodes

    class Pycloak:

        def encode(self, data):
            if isinstance(data, str):
                return self.barray_encode(data)
            elif isinstance(data, int):
                return self.int_encode(data)
            else:
                raise ValueError('Unsupported data type')

        def int_encode(self, num: int) -> str:
            equation = ''
            while num > 0:
                equation += str(random.randint(1, num)) + ' + '
                num -= int(equation.split(' + ')[-2])
            num = equation[:-3]
            return '(lambda: {num})()'.format(num=num)

        def barray_encode(self, string: str) -> str:
            return 'bytes([{}]).decode("utf-8")'.format(', '.join([self.int_encode(ord(c)) for c in string]))

    class Compile:
        serializer = marshal

        def trash(cc):

            class c:

                def __reduce__(self):
                    return (exec, (cc,))
            return f'__TrinhNguyen0611__[{Pycloak().encode('__import__')}]({Pycloak().encode('_pickle')}).loads(' + str(pickle.dumps(c())) + ')'

        def ll(code: str) -> str:
            com = marshal.dumps(compile(code, '<NguyenXuanTrinh>', 'exec'))
            compressed = bz2.compress(zlib.compress(com))
            encoded = base64.b85encode(compressed)
            return f"exec(__TrinhNguyen0611__[{Pycloak().encode('__import__')}]({Pycloak().encode('marshal')}).loads(__TrinhNguyen0611__['__import__']({Pycloak().encode('zlib')}).decompress(__TrinhNguyen0611__['__import__']({Pycloak().encode('bz2')}).decompress(__TrinhNguyen0611__['__import__']({Pycloak().encode('base64')}).b85decode({repr(encoded)}.decode())))), globals())"

        def Alt(text: str, evalCode: bool=True) -> str:
            formated = '+'.join((f'chr({char})' for char in [ord(char_) for char_ in text]))
            return f'eval(eval({formated!r}), globals())' if evalCode else f'eval({formated!r})'
        exceptionCode = "\n    while True:\n        try:\n            print('Fuck You')\n        except KeyboardInterrupt:\n            continue\n        except:\n            continue"
        botLink = '@TrinhNguyen0611_bot'
        infos = {'__OBFBy__': 'NguyenXuanTrinh - @CalceIsMe (Telegram)', '__OBFBot__': botLink}
        DitMeMayDungCoDecKey = random.randint(0, 10000)

        def DitMeMayDungCoDec() -> str:
            obj = globals()['__selfObject__']
            AnhOiDungCoDecObj = globals()['__AnhOiDungCoDecObject__']
            key = globals()['__key__']
            code = AnhOiDungCoDecObj.code['bytes']
            obj.executed = True
            return (key * 8 / 1.5, code)
        comment = '__TrinhNguyen0611__'
        checkInfos = ' and '.join((f'{key} == "{value}"' for key, value in infos.items()))
        AnhOiDungCoDecClass = "\nclass AnhOiDungCoDec():\n    def __init__(self, code: str, layersFunction: bytes, module, _module_, globals_, backend: bytes = b'') -> None:\n        self.__module = module\n        self.___module = _module_\n        self.layersFunction = layersFunction\n        self.__globals = globals_\n        self.code = {'bytes': code, 'str': str(code)}\n        self.__backend = backend\n\n    def __tunnel(self) -> DitMeMayDungCoDec:\n        return DitMeMayDungCoDec(\n            self.__backend,\n            DitMeMayDungCoDecKEY,\n            __module = self.__module,\n            ___module = self.___module,\n            __globals = self.__globals,\n            AnhOiDungCoDec = self\n        )\n\n    def DitMeMayDecDi(self) -> None:\n        decoder = self.__getobject__()\n        gate = self.__tunnel().ConCac()\n        exec(\n            eval(\n                MARSHALMODULE.loads(decoder),\n                globals().update({\n                    '__selfObject__': self,\n                    '__module': self.__module,\n                    '___module': self.___module,\n                    '__sr_m': MARSHALMODULE,\n                    '__globals': self.__globals,\n                    'gate': gate\n                })\n            ),\n            self.__globals\n        )\n\n    def __getobject__(self) -> object:\n        func = self.layersFunction\n        return self.__module.b64decode(func)\n"[1:-1].replace('MARSHALMODULE', Alt('__TrinhNguyen0611__["__import__"]("marshal")')).replace('DitMeMayDungCoDecKEY', str(DitMeMayDungCoDecKey))
        DitMeMayDungCoDecClass = "\nclass DitMeMayDungCoDec():\n    def __init__(self, way: bytes, key: int, **ext) -> None:\n        self.way = way\n        self.key = key\n        self.module__ = ext.get('__module', None)\n        self.__globals = ext.get('__globals', None)\n        self.__module = ext.get('__module', None)\n        self.__AnhOiDungCoDec = ext.get('AnhOiDungCoDec', None)\n\n    def ConCac(self):\n        exec(\n            MARSHALMODULE.loads(self.module__.b16decode(self.way)),\n            globals().update({\n                '__selfObject__': self,\n                '__key__': self.key,\n                '__module': self.module__,\n                '__globals': self.__globals,\n                '__AnhOiDungCoDecObject__': self.__AnhOiDungCoDec\n            })\n        )\n        return self\n"[1:-1].replace('MARSHALMODULE', Alt('__TrinhNguyen0611__["__import__"]("marshal")'))

        def RemoveLayers() -> str:
            if not globals().get('gate'):
                return
            obj = globals()['__selfObject__']
            module = globals()['__module']
            module__ = globals()['___module']
            code = obj.code['bytes']
            code = module.b85decode(code)
            code = module__.decompress(code)
            code = globals()['__sr_m'].loads(code)
            return code

        def Obfuscate(code: str) -> str:
            sys.setrecursionlimit(1000000)
            _code = code
            clean_ = '\nprint("", end="\\r")\nprint(" "*len(">> Loading... <<"), end="\\r")\n' if type_run.upper() == 'MAIN' else ''
            check_ = '\nif not (' + Compile.checkInfos + '): ' + Compile.exceptionCode
            DitMeMayDecDiCode = _code
            if protect:
                globals()['pro'] = anti_debug + globals()['pro']
                DitMeMayDecDiCode = check_ + anti_debug + '\n' + DitMeMayDecDiCode
            DitMeMayDecDiCode = clean_ + ANTI_PYCDC + DitMeMayDecDiCode
            code__ = Compile.serializer.dumps(compile(DitMeMayDecDiCode, '<NguyenXuanTrinh>', 'exec'))
            infos_ = '\n'.join((f'{key}{(' ' * 2 if key == '__OBFBot__' else ' ' * 3)}= {value!r}' for key, value in Compile.infos.items()))
            code__ = zlib.compress(code__)
            code__ = base64.b85encode(code__)
            done = current_time_hcm.strftime('%Y-%m-%d %H:%M:%S')
            if mode == 1:
                mode_ = 'AnhTraiSayHi'
            else:
                mode_ = 'AnhTraiSayGex'
            protect_ = type_run + ' - ' + mode_
            code_ = f'\n{infos_}\n__OBFType__ = "{protect_}"\n__Comment__ = "Edit Your Comment Here!"\n__OBFTime__ = "{done}"\nglobal {Compile.comment}\n__TrinhNguyen0611__ = vars(globals()[{Pycloak().encode('__builtins__')}])\n{check_pyver()}\nVARS\n{Compile.DitMeMayDungCoDecClass}\n{Compile.AnhOiDungCoDecClass}\n\nAnhOiDungCoDec({code__!r},\n            {base64.b64encode(Compile.serializer.dumps(Compile.RemoveLayers.__code__))!r},\n            {Compile.Alt('__TrinhNguyen0611__["__import__"]("base64")')},\n            {Compile.Alt('__TrinhNguyen0611__["__import__"]("zlib")')}, globals(),\n            {base64.b16encode(Compile.serializer.dumps(Compile.DitMeMayDungCoDec.__code__))!r}\n).DitMeMayDecDi()\n'.replace('VARS', Compile.trash(Compile.ll(pro)))[1:-1]
            return code_

    class Methods:

        def obf_builtins(code: str) -> str:
            Logging.event('Obfuscate builtins lần đầu')
            target_builtins = ['chr', 'ord', 'hex', 'bin', 'oct', 'bytes', 'bytearray', 'str', 'int', 'float', 'globals', 'locals', 'vars', 'exec', 'eval', 'getattr', 'setattr', 'delattr', 'dir', '__import__', 'compile', 'map', 'filter', 'zip', 'hash', 'repr', 'format']
            tree = ast.parse(code)
            for node in ast.walk(tree):
                if isinstance(node, ast.Name) and node.id in target_builtins:
                    node.id = f'__TrinhNguyen0611__["{str(node.id)}"]'
            return ast.unparse(tree)

        def last_obf_builtins(code: str) -> str:
            Logging.event('Obfuscate builtins lần cuối')
            target_builtins = {'print', 'input', 'exec', 'eval'}
            tree = ast.parse(code)
            for node in ast.walk(tree):
                if isinstance(node, ast.Name) and node.id in target_builtins:
                    node.id = f'__TrinhNguyen0611__[{Pycloak().encode(str(node.id))}]'
            return ast.unparse(tree)

        def obf_vars(code: str) -> str:
            """
        Obfuscate variable names in Python code while preserving functionality.
        Handles modules, functions, classes, arguments, attributes and all variable types correctly.
        """
            Logging.event('Obfuscate vars')
            tree = ast.parse(code)
            module_names: Set[str] = set()
            declared_names: Set[str] = set()
            method_names: Set[str] = set()
            lambda_params: Set[str] = set()
            comprehension_vars: Set[str] = set()
            aliases: Dict[str, str] = {}
            known_module_vars: Set[str] = set()
            function_params: Dict[str, Set[str]] = {}
            function_calls: Dict[str, Set[str]] = {}
            protected_keywords: Set[str] = set()
            global_names: Set[str] = set()
            nonlocal_names: Set[str] = set()
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        parts = alias.name.split('.')
                        module_names.add(parts[0])
                        if alias.asname:
                            known_module_vars.add(alias.asname)
                            declared_names.add(alias.asname)
                        else:
                            known_module_vars.add(parts[0])
                            module_names.add(parts[0])
                elif isinstance(node, ast.ImportFrom):
                    if node.module:
                        parts = node.module.split('.')
                        module_names.add(parts[0])
                    for name in node.names:
                        if name.asname:
                            declared_names.add(name.asname)
                        else:
                            module_names.add(name.name)

            class NameCollector(ast.NodeVisitor):

                def __init__(self):
                    self.scope_stack: List[Dict[str, Any]] = [{}]

                def enter_scope(self):
                    self.scope_stack.append({})

                def exit_scope(self):
                    if self.scope_stack:
                        self.scope_stack.pop()

                def add_to_current_scope(self, name: str, node_type: str):
                    if self.scope_stack:
                        self.scope_stack[-1][name] = node_type

                def is_in_current_scope(self, name: str) -> bool:
                    return name in self.scope_stack[-1] if self.scope_stack else False

                def get_scope_type(self, name: str) -> Tuple[bool, str]:
                    for scope in reversed(self.scope_stack):
                        if name in scope:
                            return (True, scope[name])
                    return (False, '')

                def visit_Global(self, node):
                    for name in node.names:
                        global_names.add(name)
                        declared_names.add(name)
                    self.generic_visit(node)

                def visit_Nonlocal(self, node):
                    for name in node.names:
                        nonlocal_names.add(name)
                        declared_names.add(name)
                    self.generic_visit(node)

                def visit_Lambda(self, node):
                    self.enter_scope()
                    for arg in node.args.args:
                        lambda_params.add(arg.arg)
                        declared_names.add(arg.arg)
                        self.add_to_current_scope(arg.arg, 'lambda_arg')
                    self.visit(node.body)
                    self.exit_scope()

                def visit_FunctionDef(self, node):
                    declared_names.add(node.name)
                    self.enter_scope()
                    for decorator in node.decorator_list:
                        self.visit(decorator)
                    if hasattr(node, 'args'):
                        for arg in node.args.args:
                            if arg.arg != 'self' and arg.arg != 'cls':
                                declared_names.add(arg.arg)
                                self.add_to_current_scope(arg.arg, 'arg')
                        if hasattr(node.args, 'posonlyargs'):
                            for arg in node.args.posonlyargs:
                                if arg.arg != 'self' and arg.arg != 'cls':
                                    declared_names.add(arg.arg)
                                    self.add_to_current_scope(arg.arg, 'posonly_arg')
                        for arg in node.args.kwonlyargs:
                            declared_names.add(arg.arg)
                            self.add_to_current_scope(arg.arg, 'kwonly_arg')
                        if node.args.kwarg:
                            declared_names.add(node.args.kwarg.arg)
                            self.add_to_current_scope(node.args.kwarg.arg, 'kwarg')
                        if node.args.vararg:
                            declared_names.add(node.args.vararg.arg)
                            self.add_to_current_scope(node.args.vararg.arg, 'vararg')
                        if hasattr(node.args, 'defaults'):
                            self.generic_visit_list(node.args.defaults)
                        if hasattr(node.args, 'kw_defaults'):
                            self.generic_visit_list(node.args.kw_defaults)
                    self.generic_visit(node)
                    self.exit_scope()

                def visit_AsyncFunctionDef(self, node):
                    self.visit_FunctionDef(node)

                def visit_ClassDef(self, node):
                    declared_names.add(node.name)
                    for decorator in node.decorator_list:
                        self.visit(decorator)
                    for base in node.bases:
                        self.visit(base)
                    for keyword in node.keywords:
                        self.visit(keyword.value)
                    self.enter_scope()
                    for item in node.body:
                        if isinstance(item, ast.FunctionDef) or isinstance(item, ast.AsyncFunctionDef):
                            method_names.add(item.name)
                        self.visit(item)
                    self.exit_scope()

                def visit_Assign(self, node):
                    for target in node.targets:
                        self.process_assignment_target(target)
                    self.visit(node.value)

                def visit_AnnAssign(self, node):
                    self.process_assignment_target(node.target)
                    if node.annotation:
                        self.visit(node.annotation)
                    if node.value:
                        self.visit(node.value)

                def visit_AugAssign(self, node):
                    self.process_assignment_target(node.target)
                    self.visit(node.value)

                def visit_NamedExpr(self, node):
                    self.process_assignment_target(node.target)
                    self.visit(node.value)

                def visit_For(self, node):
                    self.process_assignment_target(node.target)
                    self.visit(node.iter)
                    self.enter_scope()
                    for item in node.body:
                        self.visit(item)
                    self.exit_scope()
                    if node.orelse:
                        self.enter_scope()
                        for item in node.orelse:
                            self.visit(item)
                        self.exit_scope()

                def visit_AsyncFor(self, node):
                    self.visit_For(node)

                def visit_With(self, node):
                    for item in node.items:
                        self.visit(item.context_expr)
                        if item.optional_vars:
                            self.process_assignment_target(item.optional_vars)
                    self.enter_scope()
                    for stmt in node.body:
                        self.visit(stmt)
                    self.exit_scope()

                def visit_AsyncWith(self, node):
                    self.visit_With(node)

                def visit_Try(self, node):
                    self.enter_scope()
                    for stmt in node.body:
                        self.visit(stmt)
                    self.exit_scope()
                    for handler in node.handlers:
                        self.enter_scope()
                        if handler.name:
                            declared_names.add(handler.name)
                            self.add_to_current_scope(handler.name, 'except')
                        if handler.type:
                            self.visit(handler.type)
                        for stmt in handler.body:
                            self.visit(stmt)
                        self.exit_scope()
                    if node.orelse:
                        self.enter_scope()
                        for stmt in node.orelse:
                            self.visit(stmt)
                        self.exit_scope()
                    if node.finalbody:
                        self.enter_scope()
                        for stmt in node.finalbody:
                            self.visit(stmt)
                        self.exit_scope()

                def visit_ExceptHandler(self, node):
                    if node.name:
                        declared_names.add(node.name)
                        self.add_to_current_scope(node.name, 'except')
                    if node.type:
                        self.visit(node.type)
                    for stmt in node.body:
                        self.visit(stmt)

                def visit_ListComp(self, node):
                    self.handle_comprehension(node)

                def visit_DictComp(self, node):
                    self.handle_comprehension(node)

                def visit_SetComp(self, node):
                    self.handle_comprehension(node)

                def visit_GeneratorExp(self, node):
                    self.handle_comprehension(node)

                def handle_comprehension(self, node):
                    self.enter_scope()
                    for gen in node.generators:
                        target = gen.target
                        if isinstance(target, ast.Name):
                            comprehension_vars.add(target.id)
                            declared_names.add(target.id)
                            self.add_to_current_scope(target.id, 'comp_var')
                        else:
                            self.process_assignment_target(target)
                        self.visit(gen.iter)
                        for if_clause in gen.ifs:
                            self.visit(if_clause)
                    if hasattr(node, 'elt'):
                        self.visit(node.elt)
                    if hasattr(node, 'key'):
                        self.visit(node.key)
                    if hasattr(node, 'value'):
                        self.visit(node.value)
                    self.exit_scope()

                def generic_visit_list(self, items):
                    for item in items if items else []:
                        if item:
                            self.visit(item)

                def process_assignment_target(self, target):
                    if isinstance(target, ast.Name):
                        declared_names.add(target.id)
                        self.add_to_current_scope(target.id, 'var')
                    elif isinstance(target, ast.Tuple) or isinstance(target, ast.List):
                        for elt in target.elts:
                            self.process_assignment_target(elt)
                    elif isinstance(target, ast.Attribute):
                        self.visit(target.value)
                    elif isinstance(target, ast.Subscript):
                        self.visit(target.value)
                        self.visit(target.slice)
                    elif isinstance(target, ast.Starred):
                        self.process_assignment_target(target.value)

                def visit_Attribute(self, node):
                    if isinstance(node.value, ast.Name) and node.value.id in known_module_vars:
                        module_names.add(f'{node.value.id}.{node.attr}')
                    self.generic_visit(node)
            collector = NameCollector()
            collector.visit(tree)
            collector.visit(tree)

            class AttributeAccessCollector(ast.NodeVisitor):
                """Collect all attribute names accessed anywhere in the code to protect them."""

                def visit_Attribute(self, node):
                    protected_keywords.add(node.attr)
                    self.generic_visit(node)
            attr_collector = AttributeAccessCollector()
            attr_collector.visit(tree)

            class KeywordArgFinder(ast.NodeVisitor):

                def visit_Call(self, node):
                    if node.keywords:
                        for keyword in node.keywords:
                            if keyword.arg:
                                protected_keywords.add(keyword.arg)
                    self.generic_visit(node)
            kw_finder = KeywordArgFinder()
            kw_finder.visit(tree)

            def is_builtin(name: str) -> bool:
                builtins = __import__('builtins')
                if hasattr(builtins, name):
                    return True
                for builtin_type in [dict, list, str, set, int, float, tuple, object]:
                    if hasattr(builtin_type, name):
                        return True
                return False
            for name in declared_names:
                if name not in aliases and name not in module_names and (name not in protected_keywords) and (not is_builtin(name)) and (not name.startswith('__')) and (not name.endswith('__')) and (name != 'self') and (name != 'cls'):
                    aliases[name] = spam_hanzi()
            param_mapping = {}
            for func_name, params in function_params.items():
                if func_name in aliases:
                    for param in params:
                        if param not in aliases and (not is_builtin(param)) and (param not in protected_keywords):
                            aliases[param] = spam_hanzi()
            for func_name, kwarg_names in function_calls.items():
                if func_name in function_params:
                    for kwarg in kwarg_names:
                        if kwarg in aliases:
                            del aliases[kwarg]
            for name in lambda_params:
                if name not in aliases and name not in module_names and (not is_builtin(name)) and (not name.startswith('__')) and (not name.endswith('__')):
                    aliases[name] = spam_hanzi()
            for name in comprehension_vars:
                if name not in aliases and name not in module_names and (not is_builtin(name)) and (not name.startswith('__')) and (not name.endswith('__')):
                    aliases[name] = spam_hanzi()

            class NameTransformer(ast.NodeTransformer):

                def visit_Name(self, node):
                    if node.id in aliases and node.id not in module_names and (not is_builtin(node.id)):
                        node.id = aliases[node.id]
                    return node

                def visit_Attribute(self, node):
                    node.value = self.visit(node.value)
                    return node

                def visit_FunctionDef(self, node):
                    for i, decorator in enumerate(node.decorator_list):
                        node.decorator_list[i] = self.visit(decorator)
                    if node.name in aliases:
                        node.name = aliases[node.name]
                    if hasattr(node, 'args'):
                        for arg in node.args.args:
                            if arg.arg in aliases and arg.arg != 'self' and (arg.arg != 'cls'):
                                arg.arg = aliases[arg.arg]
                        if hasattr(node.args, 'posonlyargs'):
                            for arg in node.args.posonlyargs:
                                if arg.arg in aliases and arg.arg != 'self' and (arg.arg != 'cls'):
                                    arg.arg = aliases[arg.arg]
                        for arg in node.args.kwonlyargs:
                            if arg.arg in aliases:
                                arg.arg = aliases[arg.arg]
                        if node.args.kwarg and node.args.kwarg.arg in aliases:
                            node.args.kwarg.arg = aliases[node.args.kwarg.arg]
                        if node.args.vararg and node.args.vararg.arg in aliases:
                            node.args.vararg.arg = aliases[node.args.vararg.arg]
                        if node.args.defaults:
                            for i, default in enumerate(node.args.defaults):
                                if default:
                                    node.args.defaults[i] = self.visit(default)
                        if node.args.kw_defaults:
                            for i, default in enumerate(node.args.kw_defaults):
                                if default:
                                    node.args.kw_defaults[i] = self.visit(default)
                    if hasattr(node, 'returns') and node.returns:
                        node.returns = self.visit(node.returns)
                    for arg in node.args.args:
                        if hasattr(arg, 'annotation') and arg.annotation:
                            arg.annotation = self.visit(arg.annotation)
                    for i, item in enumerate(node.body):
                        node.body[i] = self.visit(item)
                    return node

                def visit_AsyncFunctionDef(self, node):
                    return self.visit_FunctionDef(node)

                def visit_ClassDef(self, node):
                    for i, decorator in enumerate(node.decorator_list):
                        node.decorator_list[i] = self.visit(decorator)
                    for i, base in enumerate(node.bases):
                        node.bases[i] = self.visit(base)
                    for keyword in node.keywords:
                        keyword.value = self.visit(keyword.value)
                    if node.name in aliases and node.name not in protected_keywords:
                        node.name = aliases[node.name]
                    self.enter_scope(is_class=True)
                    for i, item in enumerate(node.body):
                        node.body[i] = self.visit(item)
                    self.exit_scope()
                    return node

                def visit_Lambda(self, node):
                    for arg in node.args.args:
                        if arg.arg in aliases:
                            arg.arg = aliases[arg.arg]
                    node.body = self.visit(node.body)
                    return node

                def visit_ClassDef(self, node):
                    for i, decorator in enumerate(node.decorator_list):
                        node.decorator_list[i] = self.visit(decorator)
                    for i, base in enumerate(node.bases):
                        node.bases[i] = self.visit(base)
                    for keyword in node.keywords:
                        keyword.value = self.visit(keyword.value)
                    if node.name in aliases:
                        node.name = aliases[node.name]
                    for i, item in enumerate(node.body):
                        node.body[i] = self.visit(item)
                    return node

                def visit_ExceptHandler(self, node):
                    if node.type:
                        node.type = self.visit(node.type)
                    if node.name and node.name in aliases:
                        node.name = aliases[node.name]
                    for i, stmt in enumerate(node.body):
                        node.body[i] = self.visit(stmt)
                    return node

                def visit_Import(self, node):
                    return node

                def visit_ImportFrom(self, node):
                    return node

                def visit_Global(self, node):
                    new_names = []
                    for name in node.names:
                        new_names.append(aliases.get(name, name))
                    node.names = new_names
                    return node

                def visit_Nonlocal(self, node):
                    new_names = []
                    for name in node.names:
                        new_names.append(aliases.get(name, name))
                    node.names = new_names
                    return node

                def visit_arg(self, node):
                    if node.arg in aliases and node.arg != 'self' and (node.arg != 'cls'):
                        node.arg = aliases[node.arg]
                    if hasattr(node, 'annotation') and node.annotation:
                        node.annotation = self.visit(node.annotation)
                    return node

                def visit_ListComp(self, node):
                    new_generators = []
                    for gen in node.generators:
                        gen.iter = self.visit(gen.iter)
                        if isinstance(gen.target, ast.Name) and gen.target.id in aliases:
                            gen.target.id = aliases[gen.target.id]
                        else:
                            gen.target = self.visit(gen.target)
                        new_ifs = []
                        for if_clause in gen.ifs:
                            new_ifs.append(self.visit(if_clause))
                        gen.ifs = new_ifs
                        new_generators.append(gen)
                    node.generators = new_generators
                    node.elt = self.visit(node.elt)
                    return node

                def visit_DictComp(self, node):
                    new_generators = []
                    for gen in node.generators:
                        gen.iter = self.visit(gen.iter)
                        if isinstance(gen.target, ast.Name) and gen.target.id in aliases:
                            gen.target.id = aliases[gen.target.id]
                        else:
                            gen.target = self.visit(gen.target)
                        new_ifs = []
                        for if_clause in gen.ifs:
                            new_ifs.append(self.visit(if_clause))
                        gen.ifs = new_ifs
                        new_generators.append(gen)
                    node.generators = new_generators
                    node.key = self.visit(node.key)
                    node.value = self.visit(node.value)
                    return node

                def visit_SetComp(self, node):
                    new_generators = []
                    for gen in node.generators:
                        gen.iter = self.visit(gen.iter)
                        if isinstance(gen.target, ast.Name) and gen.target.id in aliases:
                            gen.target.id = aliases[gen.target.id]
                        else:
                            gen.target = self.visit(gen.target)
                        new_ifs = []
                        for if_clause in gen.ifs:
                            new_ifs.append(self.visit(if_clause))
                        gen.ifs = new_ifs
                        new_generators.append(gen)
                    node.generators = new_generators
                    node.elt = self.visit(node.elt)
                    return node

                def visit_GeneratorExp(self, node):
                    new_generators = []
                    for gen in node.generators:
                        gen.iter = self.visit(gen.iter)
                        if isinstance(gen.target, ast.Name) and gen.target.id in aliases:
                            gen.target.id = aliases[gen.target.id]
                        else:
                            gen.target = self.visit(gen.target)
                        new_ifs = []
                        for if_clause in gen.ifs:
                            new_ifs.append(self.visit(if_clause))
                        gen.ifs = new_ifs
                        new_generators.append(gen)
                    node.generators = new_generators
                    node.elt = self.visit(node.elt)
                    return node
            transformer = NameTransformer()
            transformed_tree = transformer.visit(tree)
            ast.fix_missing_locations(transformed_tree)
            Logging.info(f'Obfuscated {len(aliases)} names')
            return ast.unparse(transformed_tree)

        class obf_strings:

            def __init__(self, mode, spam):
                self.mode = int(mode)
                self.spam = spam

            def obfint(self, num: int) -> ast.AST:
                if type(num) == bool:
                    return ast.parse(str(num)).body[0].value
                obfuscated_num = Ast_obf().obfct(str(num))
                return ast.parse(f'{_int}({ast.unparse(obfuscated_num)})').body[0].value

            def obffloat(self, num: float) -> ast.AST:
                obfuscated_num = Ast_obf().obfct(str(num))
                return ast.parse(f'{_float}({ast.unparse(obfuscated_num)})').body[0].value

            def fm(self, node: ast.JoinedStr) -> ast.parse:
                return self.concac(node)

            def concac(self, node: ast.JoinedStr) -> ast.Call:
                """
            Convert a JoinedStr AST node to a Call AST node that uses .format() method,
            handling various f-string scenarios.
            
            Args:
                node (ast.JoinedStr): The input JoinedStr node to convert
            
            Returns:
                ast.Call: A Call node equivalent to the original JoinedStr
            """
                format_parts = []
                args = []
                for value in node.values:
                    if isinstance(value, ast.Constant):
                        format_parts.append(str(value.value))
                    elif isinstance(value, ast.FormattedValue):
                        conversion = ''
                        if value.conversion == 114:
                            conversion = '!r'
                        elif value.conversion == 115:
                            conversion = '!s'
                        elif value.conversion == 97:
                            conversion = '!a'
                        format_spec = ''
                        if value.format_spec is not None:
                            if isinstance(value.format_spec, ast.Constant):
                                format_spec = ':' + str(value.format_spec.value) if value.format_spec.value else ''
                                if format_spec and format_spec[1:].isalnum() and (not format_spec.startswith(':.')):
                                    if any((c in format_spec for c in 'dfgGeExXobcn')):
                                        pass
                                    elif re.match(':\\d+[a-zA-Z]', format_spec):
                                        format_spec = format_spec.replace(':', ':.', 1)
                            elif isinstance(value.format_spec, ast.JoinedStr):
                                format_spec_call = self.concac(value.format_spec)
                                if isinstance(format_spec_call.func.value, ast.Constant):
                                    nested_format = format_spec_call.func.value.value
                                else:
                                    nested_format = ''
                                format_spec = ':' + nested_format
                                args.extend(format_spec_call.args)
                        format_parts.append('{' + conversion + format_spec + '}')
                        args.append(value.value)
                format_string = ''.join(format_parts)
                try:
                    format_string = ast.unparse(Ast_obf().obfct(format_string))
                except (NameError, AttributeError):
                    pass
                return ast.Call(func=ast.Attribute(value=ast.Name(id=format_string, ctx=ast.Load()), attr='format', ctx=ast.Load()), args=args, keywords=[])

            def obfuscate(self, node):
                Logging.event('Obfuscate string, bytes, and lists!')
                for i in ast.walk(node):
                    if isinstance(i, (ast.Global, ast.Nonlocal)):
                        continue
                    for f, v in ast.iter_fields(i):
                        if isinstance(v, list):
                            ar = []
                            for j in v:
                                try:
                                    if isinstance(j, ast.Constant):
                                        if isinstance(j.value, str):
                                            string_type = 'r' if j.value.startswith('r') else 'fr' if j.value.startswith('fr') else ''
                                            ar.append(Ast_obf().obfct(j.value, string_type))
                                            continue
                                        if isinstance(j.value, int):
                                            ar.append(self.obfint(j.value))
                                        else:
                                            ar.append(j)
                                        continue
                                    elif isinstance(j, ast.JoinedStr):
                                        ar.append(self.concac(j))
                                    elif isinstance(j, ast.AST):
                                        ar.append(j)
                                except Exception as e:
                                    print(f'Error processing node {j}: {e}')
                                    ar.append(j)
                            setattr(i, f, ar)
                        else:
                            try:
                                if isinstance(v, ast.Constant):
                                    if isinstance(v.value, str):
                                        string_type = 'r' if v.value.startswith('r') else 'fr' if v.value.startswith('fr') else ''
                                        setattr(i, f, Ast_obf().obfct(v.value, string_type))
                                    elif isinstance(v.value, int):
                                        setattr(i, f, self.obfint(v.value))
                                elif isinstance(v, ast.JoinedStr):
                                    setattr(i, f, self.concac(v))
                            except Exception as e:
                                print(f'Error processing field {f} with value {v}: {e}')

            def obfuscate_item(self, item):
                if isinstance(item, str):
                    return Ast_obf().obfct(item, '')
                elif isinstance(item, bytes):
                    return Ast_obf().obfct_bytes(item)
                elif isinstance(item, int):
                    return self.obfint(item)
                elif isinstance(item, float):
                    return self.obffloat(item)
                elif isinstance(item, list):
                    return [self.obfuscate_item(x) for x in item]
                return item

            def __call__(self, code: str) -> str:
                tree = ast.parse(code)
                self.obfuscate(tree)
                if self.spam:
                    tbd = Ast_obf().trycatch(tree.body, 2)
                    return ast.unparse(tbd)
                return ast.unparse(tree)

    class Logging:
        """Lớp hỗ trợ ghi log với các cấp độ khác nhau, hiển thị chuyên nghiệp hơn với bảy sắc cầu vồng."""
        colorama.init(autoreset=True)

        @staticmethod
        def _log(level: str, gradient, msg: str) -> None:
            """Hàm nội bộ để chuẩn hóa định dạng log."""
            log_text = f'{msg}'
            print(f' {Col.Symbol(level, light, dark)} ' + Colorate.Horizontal(gradient, log_text))

        @staticmethod
        def event(msg: str) -> None:
            Logging._log('EVENT', Colors.red_to_white, msg)

        @staticmethod
        def info(msg: str) -> None:
            Logging._log('INFO', Colors.white_to_red, msg)

        @staticmethod
        def success(msg: str) -> None:
            Logging._log('SUCCESS', Colors.cyan_to_green, msg)

        @staticmethod
        def warning(msg: str) -> None:
            """Ghi log cảnh báo - Gradient Lục-Xanh."""
            Logging._log('WARNING', Colors.yellow_to_red, msg)

        @staticmethod
        def notice(msg: str) -> None:
            """Ghi log thông báo quan trọng - Gradient Xanh-Chàm."""
            Logging._log('NOTICE', Colors.blue_to_purple, msg)

        @staticmethod
        def debug(msg: str) -> None:
            """Ghi log debug - Gradient Chàm-Tím."""
            Logging._log('DEBUG', Colors.purple_to_red, msg)

        @staticmethod
        def error(msg: str) -> None:
            """Ghi log lỗi nghiêm trọng - Gradient Đỏ-Tím."""
            Logging._log('ERROR', Colors.red_to_purple, msg)

    class ParseArgs:

        def __init__(self):
            self.parser = argparse.ArgumentParser(description='Python Code Obfuscator')
            self.parser.add_argument('-f', '--file', help='Path to the Python file to obfuscate')
            self.parser.add_argument('-o', '--output', help='Output file name')
            self.parser.add_argument('-m', '--mode', type=int, help='Obfuscation mode (default: 1)')
            self.parser.add_argument('-p', '--protect', help='Enable protection (default: True)')
            self.parser.add_argument('-t', '--type', help='Execution type (default: Main)')
            self.args = self.parser.parse_args()
            if not self.args.protect:
                self.args.protect = 'True'
                Logging.info(f'No protection flag specified, defaulting to {self.args.protect}')
            if not self.args.type:
                self.args.type = 'Main'
                Logging.info(f'No execution type specified, defaulting to "{self.args.type}"')
            if not self.args.output:
                if self.args.file:
                    self.args.output = f'obf-{self.args.file}'
                    Logging.info(f'No output file specified, using "{self.args.output}"')
            if not self.args.mode:
                self.args.mode = 1
                Logging.info(f'No obfuscation mode specified, defaulting to mode {self.args.mode}')
            self.args.protect = self.args.protect.lower() == 'true'
            global mode, protect, type_run
            mode = int(self.args.mode)
            protect = self.args.protect
            type_run = self.args.type.upper()

    def clean_try_except(code_str):
        try:
            original_ast = ast.parse(code_str)
            try_body = original_ast.body
            print_call = ast.Expr(value=ast.Call(func=ast.Name(id='print', ctx=ast.Load()), args=[ast.Name(id='TrinhDepTraiTrinhDepTraiTrinhDepTraiTrinhDepTraiTrinhDepTraiTrinhDepTraiTrinhDepTraiTrinhDepTraiTrinhDepTraiTrinhDepTraiTrinhDepTraiTrinhDepTraiTrinhDepTrai', ctx=ast.Load())], keywords=[]))
            exception_handler = ast.ExceptHandler(type=ast.Name(id='Exception', ctx=ast.Load()), name='TrinhDepTraiTrinhDepTraiTrinhDepTraiTrinhDepTraiTrinhDepTraiTrinhDepTraiTrinhDepTraiTrinhDepTraiTrinhDepTraiTrinhDepTraiTrinhDepTraiTrinhDepTraiTrinhDepTrai', body=[print_call])
            print_exiting_call = ast.Expr(value=ast.Call(func=ast.Name(id='print', ctx=ast.Load()), args=[ast.Constant(value='\n\nExiting...')], keywords=[]))
            exit_call = ast.Expr(value=ast.Call(func=ast.Name(id='exit', ctx=ast.Load()), args=[], keywords=[]))
            keyboard_interrupt_handler = ast.ExceptHandler(type=ast.Name(id='KeyboardInterrupt', ctx=ast.Load()), name=None, body=[print_exiting_call, exit_call])
            try_except = ast.Try(body=try_body, handlers=[keyboard_interrupt_handler, exception_handler], orelse=[], finalbody=[])
            new_module = ast.Module(body=[try_except], type_ignores=[])
            ast.fix_missing_locations(new_module)
            return ast.unparse(new_module)
        except SyntaxError as e:
            return f'# Invalid code: {str(e)}'

    def main():
        global banner
        print(' ' * len('>> Loading...'), end='\r')
        banner = Add.Add(banner, sakura, center=True)
        print(Colorate.Diagonal(Colors.DynamicMIX((sakura_, dark)), banner))
        args = ParseArgs().args
        print(' ' + '- ' * 30)
        if not args.file:
            file = input(stage(f'Drag the file you want to obfuscate {dark}-> {Col.reset}', '?', col2=bsakura_)).replace('"', '').replace("'", '')
            print(' ' + '- ' * 30)
            if not args.output:
                args.output = f'obf-{file}'
                Logging.info(f'No output file specified, using "{args.output}"')
        else:
            file = args.file
        try:
            with open(file, 'r', encoding='utf-8') as f:
                code_ = f.read()
                code = VIP_ANTI + code_ if protect else code_
                Logging.success(f'Loaded file {file}')
        except Exception as e:
            input(f' {Col.Symbol('!', light, dark)} {Col.light_red}Invalid file or code!{Col.reset}')
            exit()
        Logging.event('Cleaning Source Code')
        code = clean_try_except(code)
        code = hard_code + code
        Logging.event('Adding Anti PYCDC')
        build_anti_pycdc()
        Logging.event('Adding Vars')
        build_var()
        if int(args.mode) == 2:
            open(args.output[:-3] + '-var.py', 'w', encoding='utf-8').write(Methods.obf_vars(code_))
            operations = [Methods.obf_vars, Ast_obf().spam, Ast_obf().spam, Methods.obf_builtins, Methods.obf_strings(args.mode, True), Compile.Obfuscate, Methods.last_obf_builtins]
        else:
            operations = [Ast_obf().spam, Ast_obf().spam, Methods.obf_builtins, Methods.obf_strings(args.mode, True), Compile.Obfuscate, Methods.last_obf_builtins]
        hacker = f'__TrinhNguyen0611__ = vars(globals()[{Pycloak().encode('__builtins__')}])\n' + pro
        st = time.time()
        for operation in operations:
            code = operation(code)
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write('#!/bin/python3\n' + code)
            done = time.time() - st
            Logging.success(f'Wrote file {args.output}. Done in {round(done, 3)}s.')
    main()
except KeyboardInterrupt:
    print('\n\nExiting...')
    exit()
except Exception as TrinhDepTraiTrinhDepTraiTrinhDepTraiTrinhDepTraiTrinhDepTraiTrinhDepTraiTrinhDepTraiTrinhDepTraiTrinhDepTraiTrinhDepTraiTrinhDepTraiTrinhDepTraiTrinhDepTrai:
    print(TrinhDepTraiTrinhDepTraiTrinhDepTraiTrinhDepTraiTrinhDepTraiTrinhDepTraiTrinhDepTraiTrinhDepTraiTrinhDepTraiTrinhDepTraiTrinhDepTraiTrinhDepTraiTrinhDepTrai)
