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
import colorama; colorama.init()
from datetime import datetime
import pytz
import time
import pickle
from pystyle import Colors, Colorate, Col, System, Add
from typing import Set, Dict, List, Tuple, Any, Union
import sys
System.Clear()
print('>> Loading...', end='\r')

VIP_ANTI = """
if len(globals()) != 100:
    globals()["_HOOK_CAI_LON_"]=[[[[[(('TrinhNguyen0611') * 987654321)] * 987654321] * 987654321] * 987654321] * 987654321] * 2123000000 * 2123000000
    exit()
if __import__('os').environ.get("HTTP_TOOLKIT_ACTIVE") == "true":
    globals()["_HOOK_CAI_LON_"]=[[[[[(('TrinhNguyen0611') * 987654321)] * 987654321] * 987654321] * 987654321] * 987654321] * 2123000000 * 2123000000
    exit()
for ev in ["SSL_CERT_FILE", "NODE_EXTRA_CA_CERTS", "PATH"]:
    if ev in __import__('os').environ and "httptoolkit" in __import__('os').environ[ev].lower():
        globals()["_HOOK_CAI_LON_"]=[[[[[(('TrinhNguyen0611') * 987654321)] * 987654321] * 987654321] * 987654321] * 987654321] * 2123000000 * 2123000000
        exit()
for px in ["HTTP_PROXY", "HTTPS_PROXY", "http_proxy", "https_proxy"]:
    if px in __import__('os').environ and "127.0.0.1:8000" in __import__('os').environ[px]:
        globals()["_HOOK_CAI_LON_"]=[[[[[(('TrinhNguyen0611') * 987654321)] * 987654321] * 987654321] * 987654321] * 987654321] * 2123000000 * 2123000000
        exit()
try:
    h = requests.get("https://example.com", timeout=5).headers
    if any("HTTP-Toolkit" in h.get(x, "") for x in ["Server", "Via", "X-Powered-By"]):
        globals()["_HOOK_CAI_LON_"]=[[[[[(('TrinhNguyen0611') * 987654321)] * 987654321] * 987654321] * 987654321] * 987654321] * 2123000000 * 2123000000
        exit()
except:
    pass
"""
dark = Col.white
light = Col.light_gray
sakura_ = Colors.StaticMIX((Col.red, Col.purple))
bsakura_ = Colors.StaticMIX((Col.red, Col.purple, Col.purple))
sakura = """
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣧⣼⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⢀⣀⣀⣀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⣀⣀⣀⡀⠀⠀⠀
    ⠀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⠀  Code By NguyenXuanTrinh (Aka Calce)
    ⠀⣙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣋⠀  Facebook: @Developer.NXT.IT
    ⣿⣿⣿⣿⣿⣿⣿⠁⠀⠈⠻⠿⠀⠀⠿⠟⠁⠀⠈⣿⣿⣿⣿⣿⣿⣿  Telegram: @CalceIsMe
    ⠘⢿⣿⣿⣿⣿⣿⣦⣤⣤⣄⡀⠀⠀⢀⣠⣤⣤⣴⣿⣿⣿⣿⣿⡿⠃  OBF-Bot: @TrinhNguyen0611_bot
    ⠀⠀⠙⢿⣿⣿⣿⣿⣿⠿⠋⠀⣠⣄⠀⠙⠿⣿⣿⣿⣿⣿⡿⠋⠀⠀
    ⠀⠀⠀⢰⣿⣿⣿⣿⣿⠀⠀⢠⣿⣿⡄⠀⠀⣿⣿⣿⣿⣿⡆⠀⠀⠀
    ⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀
    ⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀
    ⠀⠀⠀⠈⠛⠛⣿⣿⣿⣿⣿⡿⠛⠛⢿⣿⣿⣿⣿⣿⠛⠛⠁⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠘⠛⠛⠉⠁⠀⠀⠀⠀⠈⠉⠛⠛⠃⠀⠀⠀⠀⠀⠀
"""
banner = """
   ▄▄▄▄▄   ██   █  █▀  ▄   █▄▄▄▄ ██   
  █     ▀▄ █ █  █▄█     █  █  ▄▀ █ █  
▄  ▀▀▀▀▄   █▄▄█ █▀▄  █   █ █▀▀▌  █▄▄█ 
 ▀▄▄▄▄▀    █  █ █  █ █   █ █  █  █  █ 
              █   █  █▄ ▄█   █      █ 
             █   ▀    ▀▀▀   ▀      █  
            ▀                     ▀   
"""
def p(text):
    return print(stage(text))

def stage(text: str, symbol: str = '...', col1 = light, col2 = None) -> str:
    if col2 is None:
        col2 = light if symbol == '...' else dark
    return f""" {Col.Symbol(symbol, col1, dark)} {col2}{text}{Col.reset}"""

hcm_tz = pytz.timezone('Asia/Ho_Chi_Minh')

current_time_hcm = datetime.now(hcm_tz)

check_pyver = lambda a=".".join(__import__("sys").version.split(" ")[0].split(".")[:-1]): f'''
if ".".join(__TrinhNguyen0611__[{Pycloak().encode('__import__')}]({Pycloak().encode("sys")}).version.split(" ")[0].split(".")[:-1]) != "{a}":
    print("\\n >> Your Python is {".".join(__import__("sys").version.split(" ")[0].split(".")[:-1])}\\n You need to run this code in Python {a}\\n Using Python other than {a} won't work!\\n")
    input('Press Enter to Exit! ')
    exit(-1)
[print(c, end="", flush=True) or __TrinhNguyen0611__[{Pycloak().encode('__import__')}]({Pycloak().encode("time")}).sleep(0.01) for c in ">> Loading... <<"]
'''

anti = """
"""
global pro
global anti_debug
global ANTI_PYCDC
# anti_debug = ''
_float = "_Trinh2k10_"
_int = "_Trinh2010_"
_str = "_TrinhKhongBeDe_"
_bool = "_TrinhCuTo_"
_bytes = "_TrinhHocCode_"
__print = r"lambdaᅠ"
__input = r"execᅠ"
_eval = "_TrinhCodeHoiNgu_"
# _float = "float"
# # _lambda = "ᅠ"
# _int = "int"
# _str = "str"
# _bool = "bool"
# _bytes = "bytes"
# __print = r"tryᅠ"
# __input = r"exceptᅠ"
# _eval = "eval"
__ALIASES__ = {}
__DECLARED_NAMES__ = set()
__MODULE_NAMES__ = set()
hard_code = """
"""
list_ten_bien = [
    "TrinhSieuDepTrai", "CalceSieuCapVip", "TrinhCodeThuongThua", "CalceVoDichTheGioi",
    "TrinhChuyenGiaPro", "CalceBacThoDinhCao", "TrinhCongNgheDinh", "CalceLapTrinhMaster",
    "TrinhSangTaoVoSong", "CalceVuongGiaCode", "TrinhThuatToanHay", "CalceHackerPro",
    "TrinhThanhCongLon", "CalceToiThuongDev", "TrinhAnDanhElite", "CalceChienThanCode",
    "TrinhProMaxVIP", "CalceTruyenKyLapTrinh", "TrinhMasterMind", "CalceUltimateDev",
    "TrinhDevKing", "CalceInfinityCode", "TrinhCodeWarrior", "CalceChampionCoder",
    "TrinhCyberHero", "CalceTheBestDev", "TrinhAIWizard", "CalceOverlordCoder",
    "TrinhEliteHacker", "CalceDarkMode", "TrinhQuantumTech", "CalceGodLike"
]

def varsobf(v):
    return f"""('DitConBaGiaMay') if 2010 < 611 or 611 > 2010 or 12345 > 67890 or 98765 < 54321 or 'test' == 'false' or 0 == 1 or False == True or 1 == 2 or 10 > 20 or {random.randint(1, 1000)} > {random.randint(101, 20000000000)} else {v}"""

def spam_hanzi():
    hanzi_chars = "天地玄黄宇宙洪荒日月盈昃辰宿列张"  
    return f'__{random.randint(100000000,10000000000)}{"".join(random.choices(hanzi_chars, k=10))}{random.randint(100000000, 100000000000)}__'

def obf_gl(input_string):
    return ''.join([chr(((ord(c) - (65 if c.isupper() else 97) + 10) % 26) + (65 if c.isupper() else 97)) if c.isalpha() else c for c in input_string])

def build_anti_pycdc():
    antipycdc = ''
    e = {
        "Z": "1/0,", 
        "T": 'len+1,',  
        "N": "xyz,",  
        "T2": '"a"+1,', 
        "I": "[][99],",
        "K": '{}[""],',  
        "M": "__import__('xyz'),", 
        "V": 'int("a",99),',  
        "A": "[].__x,",  
        "F": 'open("ww"),',
    }
    for k in e: e[k] = e[k] * 1000
    # e['S'] = 'TrinhDepTrai'*1000
    # for _ in range (1000):
    antipycdc += "\n".join(f"try:({v})\nexcept:0\n" for v in e.values()) 
    
    globals()['ANTI_PYCDC'] = f"""
try:pass
except:pass
else:pass
finally:pass
{antipycdc}
finally:int(2010-611)
"""

def build_var():
    global anti_debug, pro
    concacto = open('anti.py','r',encoding='utf-8-sig').read()
    globals()['anti_debug'] = """open(__file__, "w", encoding="utf-8").write("Địt Con Bà Mày Dec Hook Cái Lồn!") if (len(open(__file__, "r", encoding="utf-8").read().split("\\n"))) != 51 else None
"""+concacto+'\n'
    pro = ANTI_PYCDC
    list_ten_bienn = [
        "TrinhSieuDepTrai", "CalceSieuCapVip", "TrinhCodeThuongThua", "CalceVoDichTheGioi",
        "TrinhChuyenGiaPro", "CalceBacThoDinhCao", "TrinhCongNgheDinh", "CalceLapTrinhMaster",
        "TrinhSangTaoVoSong", "CalceVuongGiaCode", "TrinhThuatToanHay", "CalceHackerPro",
        "TrinhThanhCongLon", "CalceToiThuongDev", "TrinhAnDanhElite", "CalceChienThanCode",
        "TrinhProMaxVIP", "CalceTruyenKyLapTrinh", "TrinhMasterMind", "CalceUltimateDev",
        "TrinhDevKing", "CalceInfinityCode", "TrinhCodeWarrior", "CalceChampionCoder",
        "TrinhCyberHero", "CalceTheBestDev", "TrinhAIWizard", "CalceOverlordCoder",
        "TrinhEliteHacker", "CalceDarkMode", "TrinhQuantumTech", "CalceGodLike"
    ]

    Hehe = [
        f"{_bool} = {varsobf('bool')}",
        f"{_str} = {varsobf('str')}",
        f"{_int} = {varsobf('int')}",
        f"{_float} = {varsobf('float')}",
        f"{_bytes} = {varsobf('bytes')}",
        f"{_eval} = {varsobf('eval')}",
        f"{__print} = {varsobf('print')}",
        f"{__input} = {varsobf('input')}"
    ]
    while ((list_ten_bienn)):
        i = random.choice(list_ten_bienn)
        hhh = random.randint(1,10)
        if hhh == 1:
            pro+= f'''globals()[''.join([chr(((ord(c) - (65 if c.isupper() else 97) - 10) % 26) + (65 if c.isupper() else 97)) if c.isalpha() else c for c in "{obf_gl(i)}"])] = lambda concacmemaybeolam, jackbocon, meomeo, bucuanhdi: (
            concacmemaybeolam.join([chr((DIT_ME_MAY - jackbocon) // meomeo) for DIT_ME_MAY in bucuanhdi])
            if concacmemaybeolam not in ["DitConBaMay", "TrinhObfuscate", "NguyenXuanTrinh"]
            else (b"" if concacmemaybeolam == "TrinhObfuscate" 
                else r"" if concacmemaybeolam == "DitConBaMay" 
                else "").join([chr((DIT_ME_MAY - jackbocon) // meomeo) for DIT_ME_MAY in bucuanhdi]))\n'''
            list_ten_bienn.remove(i)
        else:
            pro+= f'''globals()[''.join([chr(((ord(c) - (65 if c.isupper() else 97) - 10) % 26) + (65 if c.isupper() else 97)) if c.isalpha() else c for c in "{obf_gl(str('TrinhDitMeMay'))}"])] = lambda concacmemaybeolam, jackbocon, meomeo, bucuanhdi: (
            concacmemaybeolam.join([chr((DIT_ME_MAY - jackbocon) // meomeo) for DIT_ME_MAY in bucuanhdi])
            if concacmemaybeolam not in ["DitConBaMay", "TrinhObfuscate", "NguyenXuanTrinh"]
            else (b"" if concacmemaybeolam == "TrinhObfuscate" 
                else r"" if concacmemaybeolam == "DitConBaMay" 
                else "").join([chr((DIT_ME_MAY - jackbocon) // meomeo) for DIT_ME_MAY in bucuanhdi]))\n'''
            if Hehe:
                hello = random.choice(Hehe)
                pro += hello +'\n'
                Hehe.remove(hello)
        if Hehe:
            hello = random.choice(Hehe)
            pro += hello +'\n'
            Hehe.remove(hello)
class Ast_obf:

    def rn_func(self, node, ol, nn):
        for i in ast.walk(node):
            if isinstance(i, ast.FunctionDef) and i.name == ol:
                i.name = nn
            elif isinstance(i, ast.Attribute) and isinstance(i.value, ast.Name) and i.value.id == ol:
                i.value.id = nn
            elif isinstance(i, ast.Call) and isinstance(i.func, ast.Name) and i.func.id == ol:
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
                case_name = "BuConCacTaoDi"+str(random.randint(0x1E000000000, 0x7E000000000))
                case_body = [
                    ast.If(
                        test=ast.Compare(
                            left=ast.Subscript(
                                value=ast.Attribute(
                                    value=ast.Name(id=en), 
                                    attr='args'
                                ), 
                                slice=ast.Constant(value=0)
                            ), 
                            ops=[ast.Eq()], 
                            comparators=[ast.Constant(value=line)]
                        ), 
                        body=[
                            ast.Assign(
                                targets=[ast.Name(id=case_name)], 
                                value=ast.Constant(value=random.randint(0xFFFFF, 0xFFFFFFFFFFFF)), 
                                lineno=None
                            )
                        ], 
                        orelse=[]
                    )
                ]
                cases.extend(case_body)
                line += 1
            return cases

        def bl(body):
            var = "NhinCaiLon"+str(random.randint(0x1E000000000, 0x7E000000000))
            en = "NhinConCac"+str(random.randint(0x1E000000000, 0x7E000000000))

            tb = [
                ast.AugAssign(
                    target=ast.Name(id=var), 
                    op=ast.Add(), 
                    value=ast.Constant(value=1)
                ),
                ast.Try(
                    body=[
                        ast.Raise(
                            exc=ast.Call(func=ast.Name(id='MemoryError'), 
                                        args=[ast.Name(id=var)], 
                                        keywords=[])
                        )
                    ],
                    handlers=[
                        ast.ExceptHandler(
                            type=ast.Name(id='MemoryError'), 
                            name=en, 
                            body=[]
                        )
                    ],
                    orelse=[],
                    finalbody=[]
                )
            ]
            
            for i in body:
                tb[1].handlers[0].body.append(
                    ast.If(
                        test=ast.Compare(
                            left=ast.Subscript(
                                value=ast.Attribute(
                                    value=ast.Name(id=en), 
                                    attr='args'
                                ), 
                                slice=ast.Constant(value=0)
                            ), 
                            ops=[ast.Eq()], 
                            comparators=[ast.Constant(value=1)]
                        ), 
                        body=[i], 
                        orelse=[]
                    )
                )
            
            tb[1].handlers[0].body.extend(junk(en, len(body) + 1))
            
            node = ast.Assign(
                targets=[ast.Name(id=var)], 
                value=ast.Constant(value=0), 
                lineno=None
            )
            
            return [node] + tb

        def _bl(node):
            olb = node.body

            var = "__"+str(random.randint(0x1E000000000, 0x7E000000000)) + "__"
            en = "__"+str(random.randint(0x1E000000000, 0x7E000000000)) + "__"

            tb = [
                ast.AugAssign(
                    target=ast.Name(id=var), 
                    op=ast.Add(), 
                    value=ast.Constant(value=1)
                ),
                ast.Try(
                    body=[
                        ast.Raise(
                            exc=ast.Call(func=ast.Name(id='MemoryError'), 
                                        args=[ast.Name(id=var)], 
                                        keywords=[])
                        )
                    ],
                    handlers=[
                        ast.ExceptHandler(
                            type=ast.Name(id='MemoryError'), 
                            name=en, 
                            body=[]
                        )
                    ],
                    orelse=[],
                    finalbody=[]
                )
            ]
            for i in olb:
                tb[1].handlers[0].body.append(
                    ast.If(
                        test=ast.Compare(
                            left=ast.Subscript(
                                value=ast.Attribute(
                                    value=ast.Name(id=en), 
                                    attr='args'
                                ), 
                                slice=ast.Constant(value=0)
                            ), 
                            ops=[ast.Eq()], 
                            comparators=[ast.Constant(value=1)]
                        ), 
                        body=[i], 
                        orelse=[]
                    )
                )
            tb[1].handlers[0].body.extend(junk(en, len(olb) + 1))
            node.body = [
                ast.Assign(
                    targets=[ast.Name(id=var)], 
                    value=ast.Constant(value=0), 
                    lineno=None
                )
            ] + tb
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
                # Process the class body
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
                    # Recursively process nested classes
                    node.body = yuamikami_inner(node)
                    nb.append(node)
                elif isinstance(node, (ast.Assign, ast.AugAssign, ast.AnnAssign)):
                    nb.extend(bl([node]))
                elif isinstance(node, ast.Expr):
                    nb.extend(bl([node]))
                elif isinstance(node, ast.Try):
                    # Process try blocks
                    node.body = process_block(node.body)
                    # Process except handlers
                    for handler in node.handlers:
                        handler.body = process_block(handler.body)
                    # Process else block if it exists
                    if node.orelse:
                        node.orelse = process_block(node.orelse)
                    # Process finally block if it exists
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
                    # Recursively process nested try blocks
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
                    # Process try blocks at the module level
                    node.body = process_block(node.body)
                    # Process except handlers
                    for handler in node.handlers:
                        handler.body = process_block(handler.body)
                    # Process else block if it exists
                    if node.orelse:
                        node.orelse = process_block(node.orelse)
                    # Process finally block if it exists
                    if node.finalbody:
                        node.finalbody = process_block(node.finalbody)
                    nb.append(node)
                else:
                    nb.append(node)
            return nb

        nb = yuamikami(tree)
        tree.body = nb
        return tree
    
    def obfct(self, string: str, string_type: str = "") -> ast.AST:
        try:
            if string == "":
                return ast.Constant(value="")
            # if string == "NguyenXuanTrinh":
            #     return ast.Constant(value="NguyenXuanTrinh")
            dep_trai = random.choice(list_ten_bien)  
            encoded = [ord(c) * 611 + 2010 for c in string] 
            jackbocon = 2010
            meomeo = 611
            
            if string_type == 'r':  
                return ast.parse(
                    f"{_str}((lambda: {dep_trai}('DitConBaMay', {jackbocon}, {meomeo}, {encoded}))())"
                ).body[0].value
            # elif string_type == 'f':  
            #     return ast.parse(
            #         f"{_eval}((lambda: {dep_trai}('NguyenXuanTrinh', {jackbocon}, {meomeo}, {encoded}))(), locals())"
            #     ).body[0].value
                # return ast.parse(string).body[0].value
            else:
                return ast.parse(
                    f"{_str}((lambda: {dep_trai}('NguyenXuanTrinh', {jackbocon}, {meomeo}, {encoded}))())"
                ).body[0].value
                # return ast.parse(
                #     string
                # )
        except Exception as e:
            print(f"Error occurred in obfct: {str(e)}")
            return ast.Constant(value=string)  
        
    # def obfct_bytes(self, byte_data: bytes) -> ast.AST:
    #     try:
    #         if not byte_data:
    #             return ast.Constant(value=b"")

    #         dep_trai = random.choice(list_ten_bien)  
    #         encoded = [b ^ 127 for b in byte_data] 
    #         jackbocon = 127

    #         return ast.parse(
    #             f"{_bytes}((lambda: {dep_trai}('TrinhObfuscate', {jackbocon}, {encoded}))())"
    #         ).body[0].value

    #     except Exception as e:
    #         print(f"Error occurred in obfct_bytes: {str(e)}")
    #         return ast.Constant(value=byte_data)


    def random_match_case(self):
        var1 = ast.Constant(value=spam_hanzi(), kind=None)
        var2 = ast.Constant(value=spam_hanzi(), kind=None)
        return ast.Match(
            subject=ast.Compare(
                left=var1,
                ops=[ast.Eq()],
                comparators=[var2],
            ),
            cases=[
                ast.match_case(
                    pattern=ast.MatchValue(value=ast.Constant(value=True, kind=None)),
                    body=[
                        ast.Assign(
                            lineno=0,
                            col_offset=0,
                            targets=[],
                            value=ast.Raise( 
                                exc=ast.Call(
                                    func=ast.Name(id="MemoryError", ctx=ast.Load()),
                                    args=[],
                                    keywords=[ast.Constant(value=True, kind=None)], 
                                ),
                            ),
                        )
                    ],
                ),
                ast.match_case(
                    pattern=ast.MatchValue(value=ast.Constant(value=True, kind=None)),
                    body=[
                        ast.Assign(
                            lineno=0,
                            col_offset=0,
                            targets=[ast.Name(id="_" + spam_hanzi(), ctx=ast.Store())],
                            value=ast.Constant(value=[True, False], kind=None),
                        ),
                        ast.Expr(
                            lineno=0,
                            col_offset=0,
                            value=ast.Call(
                                func=ast.Name(id=_str, ctx=ast.Load()),
                                args=[ast.Constant(value="_" + spam_hanzi(), kind=None)], 
                                keywords=[],
                            ),
                        ),
                    ],
                ),
            ],
        )

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
                # Create a try block with a random match-case statement
                # and wrap the current_node in an except handler
                try_block = ast.Try(
                    body=[
                        self.random_match_case(),
                        # Add a raise statement at the end of the try block
                        ast.Raise(
                            exc=ast.Call(
                                func=ast.Name(id="MemoryError", ctx=ast.Load()),
                                args=[],
                                keywords=[],
                                # keywords=[ast.keyword(arg=None, value=ast.Constant(value=True))],
                            ),
                            cause=None,
                        )
                    ],
                    handlers=[
                        # Create an except handler for MemoryError
                        ast.ExceptHandler(
                            type=ast.Name(id="MemoryError", ctx=ast.Load()),
                            name="_" + spam_hanzi(),  # Generate a random variable name
                            body=[current_node],
                        )
                    ],
                    orelse=[],  # No else clause
                    finalbody=[],  # No finally clause
                )
                
                # Update current_node to be the newly created try-except block
                current_node = try_block
            
            # Add the final wrapped node to the result list
            result_nodes.append(current_node)
        
        return result_nodes

class Pycloak:
    def encode(self, data):
        if isinstance(data, str):
            return self.barray_encode(data) 
        elif isinstance(data, int):
            return self.int_encode(data)
        else:
            raise ValueError("Unsupported data type")
    
    def int_encode(self, num: int) -> str:
        equation = ''
        while num > 0:
            equation += str(random.randint(1, num)) + ' + '
            num -= int(equation.split(' + ')[-2])
        num = equation[:-3]
        return '(lambda: {num})()'.format(num=num)

    def barray_encode(self, string: str) -> str:
        return 'bytes([{}]).decode("utf-8")'.format(', '.join([self.int_encode(ord(c)) for c in string]))

class Compile():

    serializer = marshal
    def trash(cc):
        class c:
            def __reduce__(self):
                return (exec, (cc,))
        return f"__TrinhNguyen0611__[{Pycloak().encode('__import__')}]({Pycloak().encode('_pickle')}).loads(" + str(pickle.dumps(c())) + ")"

    def ll(code: str) -> str:
        com = marshal.dumps(compile(code, "<NguyenXuanTrinh>", "exec"))
        compressed = bz2.compress(zlib.compress(com))
        encoded = base64.b85encode(compressed)
        return f"exec(__TrinhNguyen0611__[{Pycloak().encode('__import__')}]({Pycloak().encode('marshal')}).loads(__TrinhNguyen0611__['__import__']({Pycloak().encode('zlib')}).decompress(__TrinhNguyen0611__['__import__']({Pycloak().encode('bz2')}).decompress(__TrinhNguyen0611__['__import__']({Pycloak().encode('base64')}).b85decode({repr(encoded)}.decode())))), globals())"
    def Alt(text: str, evalCode: bool = True) -> str:
        formated = '+'.join(f'chr({char})' for char in [ord(char_) for char_ in text])
        return f'eval(eval({formated!r}), globals())' if evalCode else f'eval({formated!r})'
    exceptionCode = """
    while True:
        try:
            print('Fuck You')
        except KeyboardInterrupt:
            continue
        except:
            continue"""
    botLink = "@TrinhNguyen0611_bot"
    infos = {
        '__OBFBy__': "NguyenXuanTrinh - @CalceIsMe (Telegram)",
        '__OBFBot__': botLink,
    } 
    DitMeMayDungCoDecKey = random.randint(0, 10000)
    def DitMeMayDungCoDec() -> str:
        obj = globals()['__selfObject__']
        AnhOiDungCoDecObj = globals()['__AnhOiDungCoDecObject__']
        key = globals()['__key__']
        code = AnhOiDungCoDecObj.code['bytes']
        obj.executed = True
        return ((key * 8 / 1.5), code)
    comment = '__TrinhNguyen0611__'
    
    checkInfos = ' and '.join(f'{key} == "{(value)}"' for key, value in infos.items())
    AnhOiDungCoDecClass = """
class AnhOiDungCoDec():
    def __init__(self, code: str, layersFunction: bytes, module, _module_, globals_, backend: bytes = b'') -> None:
        self.__module = module
        self.___module = _module_
        self.layersFunction = layersFunction
        self.__globals = globals_
        self.code = {'bytes': code, 'str': str(code)}
        self.__backend = backend

    def __tunnel(self) -> DitMeMayDungCoDec:
        return DitMeMayDungCoDec(
            self.__backend,
            DitMeMayDungCoDecKEY,
            __module = self.__module,
            ___module = self.___module,
            __globals = self.__globals,
            AnhOiDungCoDec = self
        )

    def DitMeMayDecDi(self) -> None:
        decoder = self.__getobject__()
        gate = self.__tunnel().ConCac()
        exec(
            eval(
                MARSHALMODULE.loads(decoder),
                globals().update({
                    '__selfObject__': self,
                    '__module': self.__module,
                    '___module': self.___module,
                    '__sr_m': MARSHALMODULE,
                    '__globals': self.__globals,
                    'gate': gate
                })
            ),
            self.__globals
        )

    def __getobject__(self) -> object:
        func = self.layersFunction
        return self.__module.b64decode(func)
"""[1:-1].replace('MARSHALMODULE', Alt('__TrinhNguyen0611__["__import__"]("marshal")')).replace('DitMeMayDungCoDecKEY', str(DitMeMayDungCoDecKey))

    DitMeMayDungCoDecClass = """
class DitMeMayDungCoDec():
    def __init__(self, way: bytes, key: int, **ext) -> None:
        self.way = way
        self.key = key
        self.module__ = ext.get('__module', None)
        self.__globals = ext.get('__globals', None)
        self.__module = ext.get('__module', None)
        self.__AnhOiDungCoDec = ext.get('AnhOiDungCoDec', None)

    def ConCac(self):
        exec(
            MARSHALMODULE.loads(self.module__.b16decode(self.way)),
            globals().update({
                '__selfObject__': self,
                '__key__': self.key,
                '__module': self.module__,
                '__globals': self.__globals,
                '__AnhOiDungCoDecObject__': self.__AnhOiDungCoDec
            })
        )
        return self
"""[1:-1].replace('MARSHALMODULE', Alt('__TrinhNguyen0611__["__import__"]("marshal")'))
    def RemoveLayers() -> str:
        if not globals().get('gate'): return
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
        # _code = 
        clean_ = """
print("", end="\\r")
print(" "*len(">> Loading... <<"), end="\\r")
""" if type_run.upper() == 'MAIN' else ""
        check_ = """
if not ("""+Compile.checkInfos+"""): """+Compile.exceptionCode
        DitMeMayDecDiCode = _code
        if protect:
            globals()['pro'] = anti_debug + globals()['pro']
            DitMeMayDecDiCode = check_ + anti_debug + '\n' + DitMeMayDecDiCode
        DitMeMayDecDiCode = clean_ + ANTI_PYCDC + DitMeMayDecDiCode
        # return DitMeMayDecDiCode
        code__ = Compile.serializer.dumps(compile(DitMeMayDecDiCode, '<NguyenXuanTrinh>', 'exec'))
        infos_ = '\n'.join(f"{key}{' ' * 2 if key == '__OBFBot__' else ' ' * 3}= {value!r}" for key, value in Compile.infos.items())
        code__ = zlib.compress(code__)
        code__ = base64.b85encode(code__)
        done = current_time_hcm.strftime('%Y-%m-%d %H:%M:%S')
        if mode == 1:
            mode_ = "AnhTraiSayHi"
        else:
            mode_ = "AnhTraiSayGex"
        protect_ = type_run + ' - ' + mode_
        code_ = f'''
{infos_}
__OBFType__ = "{protect_}"
__Comment__ = "Edit Your Comment Here!"
__OBFTime__ = "{done}"
global {Compile.comment}
__TrinhNguyen0611__ = vars(globals()[{Pycloak().encode('__builtins__')}])
{check_pyver()}
VARS
{Compile.DitMeMayDungCoDecClass}
{Compile.AnhOiDungCoDecClass}

AnhOiDungCoDec({code__!r},
            {base64.b64encode(Compile.serializer.dumps(Compile.RemoveLayers.__code__))!r},
            {Compile.Alt('__TrinhNguyen0611__["__import__"]("base64")')},
            {Compile.Alt('__TrinhNguyen0611__["__import__"]("zlib")')}, globals(),
            {base64.b16encode(Compile.serializer.dumps(Compile.DitMeMayDungCoDec.__code__))!r}
).DitMeMayDecDi()
'''.replace('VARS',  Compile.trash(Compile.ll(pro)))[1:-1]
        return code_
        
class Methods:
    def obf_builtins(code: str) -> str:
        Logging.event('Obfuscate builtins lần đầu')
        target_builtins = [
            'chr', 'ord', 'hex', 'bin', 'oct',  # Xử lý mã hóa ký tự
            'bytes', 'bytearray',               # Làm việc với dữ liệu nhị phân
            'str', 'int', 'float',               # Kiểu dữ liệu cơ bản
            'globals', 'locals', 'vars',         # Truy cập biến môi trường
            'exec', 'eval',                      # Thực thi mã động
            'getattr', 'setattr', 'delattr',      # Truy xuất và thay đổi thuộc tính
            'dir', '__import__', 'compile',      # Nạp và biên dịch mã động
            'map', 'filter', 'zip',              # Các hàm xử lý danh sách
            'hash', 'repr', 'format'       # Các hàm tiện ích
        ]
        tree = ast.parse(code)
        for node in ast.walk(tree):
            if isinstance(node, ast.Name) and node.id in target_builtins:
                node.id = f'__TrinhNguyen0611__["{(str(node.id))}"]'

        return ast.unparse(tree)
    def last_obf_builtins(code: str) -> str:
        Logging.event('Obfuscate builtins lần cuối')
        target_builtins = {
            "print", "input", "exec", "eval"
        }
        tree = ast.parse(code)
        for node in ast.walk(tree):
            if isinstance(node, ast.Name) and node.id in target_builtins:
                node.id = f'__TrinhNguyen0611__[{(Pycloak().encode(str(node.id)))}]'
        return ast.unparse(tree)

    def obf_vars(code: str) -> str:
        """
        Obfuscate variable names in Python code while preserving functionality.
        Handles modules, functions, classes, arguments, attributes and all variable types correctly.
        """
        
        # Assume Logging and spam_hanzi are defined elsewhere
        Logging.event('Obfuscate vars')
        
        # Parse the code
        tree = ast.parse(code)
        
        # Define name collections
        module_names: Set[str] = set()
        declared_names: Set[str] = set()
        method_names: Set[str] = set()
        lambda_params: Set[str] = set()
        comprehension_vars: Set[str] = set()
        aliases: Dict[str, str] = {}
        
        # Track known modules to protect their attributes from obfuscation
        known_module_vars: Set[str] = set()
        
        # Track function parameters to ensure consistent obfuscation
        function_params: Dict[str, Set[str]] = {}
        function_calls: Dict[str, Set[str]] = {}
        
        # Collect keyword arguments that should never be obfuscated
        protected_keywords: Set[str] = set()
        
        # Analyze global and nonlocal declarations
        global_names: Set[str] = set()
        nonlocal_names: Set[str] = set()
        
        # This approach to obfuscation has more edge cases than anticipated
        # A more reliable approach is to create a safelist of names that should never be obfuscated
        # Alongside with careful tracking of function parameters and keyword arguments
        
        # Safelist includes:
        # - Module names and imported names
        # - Builtin names and methods
        # - Special names (__x__)
        # - 'self' and 'cls'
        # - All keyword argument names used anywhere in the code
        
        # First pass: collect module imports
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    # Handle all parts of a multi-part import
                    parts = alias.name.split('.')
                    module_names.add(parts[0])
                    # Track the asname if provided, or the original name
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
                # Track imported names and their aliases
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
                # Search from innermost to outermost scope
                for scope in reversed(self.scope_stack):
                    if name in scope:
                        return True, scope[name]
                return False, ""
                
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
                # Enter a new scope for the lambda
                self.enter_scope()
                
                # Process lambda arguments
                for arg in node.args.args:
                    lambda_params.add(arg.arg)
                    declared_names.add(arg.arg)
                    self.add_to_current_scope(arg.arg, 'lambda_arg')
                    
                # Process lambda body
                self.visit(node.body)
                
                # Exit lambda scope
                self.exit_scope()
                
            def visit_FunctionDef(self, node):
                declared_names.add(node.name)
                
                # Enter new scope
                self.enter_scope()
                
                # Process decorators
                for decorator in node.decorator_list:
                    self.visit(decorator)
                
                # Process arguments
                if hasattr(node, 'args'):
                    for arg in node.args.args:
                        if arg.arg != 'self' and arg.arg != 'cls':
                            declared_names.add(arg.arg)
                            self.add_to_current_scope(arg.arg, 'arg')
                    
                    # Handle posonlyargs (Python 3.8+)
                    if hasattr(node.args, 'posonlyargs'):
                        for arg in node.args.posonlyargs:
                            if arg.arg != 'self' and arg.arg != 'cls':
                                declared_names.add(arg.arg)
                                self.add_to_current_scope(arg.arg, 'posonly_arg')
                    
                    # Handle kwonlyargs
                    for arg in node.args.kwonlyargs:
                        declared_names.add(arg.arg)
                        self.add_to_current_scope(arg.arg, 'kwonly_arg')
                    
                    # Handle kwargs
                    if node.args.kwarg:
                        declared_names.add(node.args.kwarg.arg)
                        self.add_to_current_scope(node.args.kwarg.arg, 'kwarg')
                        
                    # Handle varargs
                    if node.args.vararg:
                        declared_names.add(node.args.vararg.arg)
                        self.add_to_current_scope(node.args.vararg.arg, 'vararg')
                        
                    # Handle default arguments
                    if hasattr(node.args, 'defaults'):
                        self.generic_visit_list(node.args.defaults)
                    
                    # Handle kw_defaults
                    if hasattr(node.args, 'kw_defaults'):
                        self.generic_visit_list(node.args.kw_defaults)
                    
                # Process function body
                self.generic_visit(node)
                
                # Exit scope
                self.exit_scope()
                
            def visit_AsyncFunctionDef(self, node):
                # Handle async functions the same as regular functions
                self.visit_FunctionDef(node)
                
            def visit_ClassDef(self, node):
                declared_names.add(node.name)
                
                # Process decorators
                for decorator in node.decorator_list:
                    self.visit(decorator)
                
                # Process base classes and keywords
                for base in node.bases:
                    self.visit(base)
                for keyword in node.keywords:
                    self.visit(keyword.value)
                
                # Enter new scope
                self.enter_scope()
                
                # Visit class body
                for item in node.body:
                    if isinstance(item, ast.FunctionDef) or isinstance(item, ast.AsyncFunctionDef):
                        method_names.add(item.name)
                    self.visit(item)
                
                # Exit scope
                self.exit_scope()
                
            def visit_Assign(self, node):
                # Process targets
                for target in node.targets:
                    self.process_assignment_target(target)
                
                # Process the value
                self.visit(node.value)
                
            def visit_AnnAssign(self, node):
                # Process annotated assignments
                self.process_assignment_target(node.target)
                
                # Visit annotation
                if node.annotation:
                    self.visit(node.annotation)
                    
                # Visit value if it exists
                if node.value:
                    self.visit(node.value)
                
            def visit_AugAssign(self, node):
                # Process augmented assignments (e.g., x += 1)
                self.process_assignment_target(node.target)
                self.visit(node.value)
                
            def visit_NamedExpr(self, node):
                # Process assignment expressions (walrus operator, :=)
                self.process_assignment_target(node.target)
                self.visit(node.value)
                
            def visit_For(self, node):
                # Process the target of a for loop
                self.process_assignment_target(node.target)
                self.visit(node.iter)
                
                # Enter new scope for the body
                self.enter_scope()
                for item in node.body:
                    self.visit(item)
                self.exit_scope()
                
                # Visit the else clause if it exists
                if node.orelse:
                    self.enter_scope()
                    for item in node.orelse:
                        self.visit(item)
                    self.exit_scope()
                    
            def visit_AsyncFor(self, node):
                # Handle async for loops the same as regular for loops
                self.visit_For(node)
                    
            def visit_With(self, node):
                # Process with items
                for item in node.items:
                    self.visit(item.context_expr)
                    if item.optional_vars:
                        self.process_assignment_target(item.optional_vars)
                
                # Enter new scope for the body
                self.enter_scope()
                for stmt in node.body:
                    self.visit(stmt)
                self.exit_scope()
                
            def visit_AsyncWith(self, node):
                # Handle async with statements the same as regular with statements
                self.visit_With(node)
                
            def visit_Try(self, node):
                # Process try block
                self.enter_scope()
                for stmt in node.body:
                    self.visit(stmt)
                self.exit_scope()
                
                # Process except handlers
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
                    
                # Process else block
                if node.orelse:
                    self.enter_scope()
                    for stmt in node.orelse:
                        self.visit(stmt)
                    self.exit_scope()
                    
                # Process finally block
                if node.finalbody:
                    self.enter_scope()
                    for stmt in node.finalbody:
                        self.visit(stmt)
                    self.exit_scope()
                    
            def visit_ExceptHandler(self, node):
                # Handle the exception variable
                if node.name:
                    declared_names.add(node.name)
                    self.add_to_current_scope(node.name, 'except')
                
                # Visit exception type if it exists
                if node.type:
                    self.visit(node.type)
                    
                # Visit handler body
                for stmt in node.body:
                    self.visit(stmt)
                    
            def visit_ListComp(self, node):
                # Handle list comprehensions
                self.handle_comprehension(node)
                
            def visit_DictComp(self, node):
                # Handle dictionary comprehensions
                self.handle_comprehension(node)
                
            def visit_SetComp(self, node):
                # Handle set comprehensions
                self.handle_comprehension(node)
                
            def visit_GeneratorExp(self, node):
                # Handle generator expressions
                self.handle_comprehension(node)
                
            def handle_comprehension(self, node):
                # Enter a new scope for the comprehension
                self.enter_scope()
                
                # Process generators
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
                        
                # Process the element (and key/value for dict comps)
                if hasattr(node, 'elt'):
                    self.visit(node.elt)
                if hasattr(node, 'key'):
                    self.visit(node.key)
                if hasattr(node, 'value'):
                    self.visit(node.value)
                    
                # Exit the comprehension scope
                self.exit_scope()
                
            def generic_visit_list(self, items):
                for item in items if items else []:
                    if item:  # Handle None values in kw_defaults
                        self.visit(item)
                        
            def process_assignment_target(self, target):
                if isinstance(target, ast.Name):
                    declared_names.add(target.id)
                    self.add_to_current_scope(target.id, 'var')
                elif isinstance(target, ast.Tuple) or isinstance(target, ast.List):
                    for elt in target.elts:
                        self.process_assignment_target(elt)
                elif isinstance(target, ast.Attribute):
                    # We don't add attributes to declared_names here
                    # because we only want to rename attributes that are
                    # already in our aliases (usually declared as variables)
                    self.visit(target.value)
                elif isinstance(target, ast.Subscript):
                    # Handle cases like a[b] = c
                    self.visit(target.value)
                    self.visit(target.slice)
                elif isinstance(target, ast.Starred):
                    # Handle starred assignments like a, *b = c
                    self.process_assignment_target(target.value)
                    
            # Track module attributes to preserve them
            def visit_Attribute(self, node):
                if isinstance(node.value, ast.Name) and node.value.id in known_module_vars:
                    # This is a module attribute access, mark it to be preserved
                    module_names.add(f"{node.value.id}.{node.attr}")
                self.generic_visit(node)
        
        # Collect all names
        # First make a pass to collect function definitions and calls
        collector = NameCollector()
        collector.visit(tree)
        
        # Second pass to collect function calls for functions not seen in first pass
        collector.visit(tree)
        
        # Now find all attribute access and protect those names too
        class AttributeAccessCollector(ast.NodeVisitor):
            """Collect all attribute names accessed anywhere in the code to protect them."""
            def visit_Attribute(self, node):
                # Add all attribute names to protected_keywords
                protected_keywords.add(node.attr)
                self.generic_visit(node)
        
        # Collect and protect all attribute names
        attr_collector = AttributeAccessCollector()
        attr_collector.visit(tree)
        
        # Also collect keyword arguments
        class KeywordArgFinder(ast.NodeVisitor):
            def visit_Call(self, node):
                if node.keywords:
                    for keyword in node.keywords:
                        # Add all keyword argument names to the protected set
                        if keyword.arg:
                            protected_keywords.add(keyword.arg)
                self.generic_visit(node)
        
        # Run the keyword finder to explicitly protect all keywords
        kw_finder = KeywordArgFinder()
        kw_finder.visit(tree)
        
        # Check if a name is a Python builtin or a method of a builtin type
        def is_builtin(name: str) -> bool:
            builtins = __import__('builtins')
            # Check if it's a builtin name
            if hasattr(builtins, name):
                return True
            
            # Check if it's a method of common builtin types
            for builtin_type in [dict, list, str, set, int, float, tuple, object]:
                if hasattr(builtin_type, name):
                    return True
            
            return False
        
        # Create aliases for declared names that aren't special
        for name in declared_names:
            if (name not in aliases and 
                name not in module_names and 
                name not in protected_keywords and  # Don't obfuscate protected keywords
                not is_builtin(name) and
                not name.startswith('__') and 
                not name.endswith('__') and
                name != 'self' and
                name != 'cls'):
                aliases[name] = spam_hanzi()
                
        # DO NOT create aliases for method names - methods need to remain accessible
        # This prevents issues with method lookup on objects
        # Skip this and leave all method names intact
        
        # Ensure parameter names are consistent between function calls and definitions
        # First, create direct parameter mapping
        param_mapping = {}
        for func_name, params in function_params.items():
            if func_name in aliases:  # The function name will be obfuscated
                # Create consistent mappings for each parameter
                for param in params:
                    if (param not in aliases and 
                        not is_builtin(param) and 
                        param not in protected_keywords):  # Don't obfuscate protected keywords
                        aliases[param] = spam_hanzi()
                        
        # Make sure keyword arguments match their parameter names
        for func_name, kwarg_names in function_calls.items():
            if func_name in function_params:
                # For each keyword used in a call to this function
                for kwarg in kwarg_names:
                    # Don't obfuscate keyword argument names - they need to match parameters
                    # Remove them from aliases if they were added
                    if kwarg in aliases:
                        del aliases[kwarg]
                
        # Create aliases for lambda parameters
        for name in lambda_params:
            if (name not in aliases and 
                name not in module_names and 
                not is_builtin(name) and
                not name.startswith('__') and 
                not name.endswith('__')):
                aliases[name] = spam_hanzi()
                
        # Create aliases for comprehension variables
        for name in comprehension_vars:
            if (name not in aliases and 
                name not in module_names and 
                not is_builtin(name) and
                not name.startswith('__') and 
                not name.endswith('__')):
                aliases[name] = spam_hanzi()
        
        # Transformer to rename variables
        class NameTransformer(ast.NodeTransformer):
            def visit_Name(self, node):
                # Rename variables but preserve builtins and modules
                if (node.id in aliases and 
                    node.id not in module_names and 
                    not is_builtin(node.id)):
                    node.id = aliases[node.id]
                return node
                
            def visit_Attribute(self, node):
                # Visit the value first (e.g., object in object.attr)
                node.value = self.visit(node.value)
                
                # NEVER obfuscate attributes, especially:
                # 1. Don't rename if it's a dunder method (__x__)
                # 2. Don't rename if it's a builtin attribute or method of a builtin type
                # 3. Don't rename module attributes we've tracked
                # 4. Don't rename class methods/attributes as they need to be consistent
                
                # The safest approach is to never obfuscate any attribute access
                # This ensures methods like self.AddBuiltins() remain functional
                
                return node
                
            def visit_FunctionDef(self, node):
                # Visit decorators first
                for i, decorator in enumerate(node.decorator_list):
                    node.decorator_list[i] = self.visit(decorator)
                    
                # Rename function name if it's in our aliases
                if node.name in aliases:
                    node.name = aliases[node.name]
                    
                # Rename arguments
                if hasattr(node, 'args'):
                    # Regular args
                    for arg in node.args.args:
                        if arg.arg in aliases and arg.arg != 'self' and arg.arg != 'cls':
                            arg.arg = aliases[arg.arg]
                            
                    # Position-only args (Python 3.8+)
                    if hasattr(node.args, 'posonlyargs'):
                        for arg in node.args.posonlyargs:
                            if arg.arg in aliases and arg.arg != 'self' and arg.arg != 'cls':
                                arg.arg = aliases[arg.arg]
                    
                    # Keyword-only args
                    for arg in node.args.kwonlyargs:
                        if arg.arg in aliases:
                            arg.arg = aliases[arg.arg]
                    
                    # Handle kwargs
                    if node.args.kwarg and node.args.kwarg.arg in aliases:
                        node.args.kwarg.arg = aliases[node.args.kwarg.arg]
                        
                    # Handle varargs
                    if node.args.vararg and node.args.vararg.arg in aliases:
                        node.args.vararg.arg = aliases[node.args.vararg.arg]
                        
                    # Visit default values
                    if node.args.defaults:
                        for i, default in enumerate(node.args.defaults):
                            if default:
                                node.args.defaults[i] = self.visit(default)
                                
                    # Visit keyword default values
                    if node.args.kw_defaults:
                        for i, default in enumerate(node.args.kw_defaults):
                            if default:
                                node.args.kw_defaults[i] = self.visit(default)
                
                # Process annotations if they exist
                if hasattr(node, 'returns') and node.returns:
                    node.returns = self.visit(node.returns)
                    
                for arg in node.args.args:
                    if hasattr(arg, 'annotation') and arg.annotation:
                        arg.annotation = self.visit(arg.annotation)
                
                # Process the function body
                for i, item in enumerate(node.body):
                    node.body[i] = self.visit(item)
                    
                return node
                
            def visit_AsyncFunctionDef(self, node):
                # Use the same logic as for regular function defs
                return self.visit_FunctionDef(node)
                
            def visit_ClassDef(self, node):
                # First visit decorators
                for i, decorator in enumerate(node.decorator_list):
                    node.decorator_list[i] = self.visit(decorator)
                    
                # Visit base classes
                for i, base in enumerate(node.bases):
                    node.bases[i] = self.visit(base)
                    
                # Visit keyword arguments
                for keyword in node.keywords:
                    keyword.value = self.visit(keyword.value)
                    
                # Rename class name if it's in our aliases and not protected
                if node.name in aliases and node.name not in protected_keywords:
                    node.name = aliases[node.name]
                    
                # Enter class scope
                self.enter_scope(is_class=True)
                
                # Process the class body
                for i, item in enumerate(node.body):
                    node.body[i] = self.visit(item)
                    
                # Exit class scope
                self.exit_scope()
                    
                return node
                
            def visit_Lambda(self, node):
                # Process arguments
                for arg in node.args.args:
                    if arg.arg in aliases:
                        arg.arg = aliases[arg.arg]
                        
                # Process body
                node.body = self.visit(node.body)
                return node
                
            def visit_ClassDef(self, node):
                # Visit decorators
                for i, decorator in enumerate(node.decorator_list):
                    node.decorator_list[i] = self.visit(decorator)
                    
                # Visit base classes
                for i, base in enumerate(node.bases):
                    node.bases[i] = self.visit(base)
                    
                # Visit keywords
                for keyword in node.keywords:
                    keyword.value = self.visit(keyword.value)
                    
                # Rename class name if it's in our aliases
                if node.name in aliases:
                    node.name = aliases[node.name]
                    
                # Process the class body
                for i, item in enumerate(node.body):
                    node.body[i] = self.visit(item)
                    
                return node
                
            def visit_ExceptHandler(self, node):
                # Visit the exception type
                if node.type:
                    node.type = self.visit(node.type)
                    
                # Rename the exception variable
                if node.name and node.name in aliases:
                    node.name = aliases[node.name]
                    
                # Visit the body
                for i, stmt in enumerate(node.body):
                    node.body[i] = self.visit(stmt)
                    
                return node
                
            def visit_Import(self, node):
                # Preserve import statements
                return node
                
            def visit_ImportFrom(self, node):
                # Preserve import statements
                return node
                
            def visit_Global(self, node):
                # Update global statement names
                new_names = []
                for name in node.names:
                    new_names.append(aliases.get(name, name))
                node.names = new_names
                return node
                
            def visit_Nonlocal(self, node):
                # Update nonlocal statement names
                new_names = []
                for name in node.names:
                    new_names.append(aliases.get(name, name))
                node.names = new_names
                return node
                
            def visit_arg(self, node):
                # Rename function arguments
                if node.arg in aliases and node.arg != 'self' and node.arg != 'cls':
                    node.arg = aliases[node.arg]
                    
                # Visit annotation if it exists
                if hasattr(node, 'annotation') and node.annotation:
                    node.annotation = self.visit(node.annotation)
                    
                return node
                
            def visit_ListComp(self, node):
                # Process comprehension nodes with their own scope
                new_generators = []
                for gen in node.generators:
                    # Visit the iterator
                    gen.iter = self.visit(gen.iter)
                    
                    # Rename the target
                    if isinstance(gen.target, ast.Name) and gen.target.id in aliases:
                        gen.target.id = aliases[gen.target.id]
                    else:
                        gen.target = self.visit(gen.target)
                        
                    # Visit if clauses
                    new_ifs = []
                    for if_clause in gen.ifs:
                        new_ifs.append(self.visit(if_clause))
                    gen.ifs = new_ifs
                    
                    new_generators.append(gen)
                    
                node.generators = new_generators
                node.elt = self.visit(node.elt)
                return node
                
            def visit_DictComp(self, node):
                # Handle dictionary comprehensions like list comprehensions
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
                # Handle set comprehensions like list comprehensions
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
                # Handle generator expressions like list comprehensions
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
        
        # Apply the transformer
        transformer = NameTransformer()
        transformed_tree = transformer.visit(tree)
        
        # Fix any AST issues
        ast.fix_missing_locations(transformed_tree)
        
        # Create a debug log of what was obfuscated
        Logging.info(f"Obfuscated {len(aliases)} names")
        
        # Return the unparsed code
        return ast.unparse(transformed_tree)

    class obf_strings:
        def __init__(self, mode, spam):
            self.mode = int(mode)
            self.spam = spam

        def obfint(self, num: int) -> ast.AST:
            if type(num) == bool:
                # obfuscated_bool = Ast_obf().obfct(str(num)) 
                # return ast.parse(f"{_eval}({ast.unparse(obfuscated_bool)})").body[0].value
                return ast.parse(str(num)).body[0].value
            
            obfuscated_num = Ast_obf().obfct(str(num)) 
            return ast.parse(f"{_int}({ast.unparse(obfuscated_num)})").body[0].value
            
        def obffloat(self, num: float) -> ast.AST:
            obfuscated_num = Ast_obf().obfct(str(num))  


            return ast.parse(f"{_float}({ast.unparse(obfuscated_num)})").body[0].value
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
            # Prepare format string and arguments
            format_parts = []
            args = []
            
            for value in node.values:
                if isinstance(value, ast.Constant):
                    # Regular string constant
                    format_parts.append(str(value.value))
                elif isinstance(value, ast.FormattedValue):
                    # Determine conversion flag and format spec
                    conversion = ""
                    if value.conversion == 114:  # 'r' - repr
                        conversion = "!r"
                    elif value.conversion == 115:  # 's' - str
                        conversion = "!s"
                    elif value.conversion == 97:   # 'a' - ascii
                        conversion = "!a"
                    
                    # Handle format spec
                    format_spec = ""
                    if value.format_spec is not None:
                        if isinstance(value.format_spec, ast.Constant):
                            # Simple string format spec (like .1f, d, etc.)
                            format_spec = ":" + str(value.format_spec.value) if value.format_spec.value else ""
                            # Special handling for format specs that don't include the leading dot
                            if format_spec and format_spec[1:].isalnum() and not format_spec.startswith(":."):
                                # Check if this is likely a numeric format like 'd', 'f', etc.
                                if any(c in format_spec for c in "dfgGeExXobcn"):
                                    # It's a numeric format without leading precision - leave as is
                                    pass
                                # For cases like ":1f" that should be ":.1f"
                                elif re.match(r":\d+[a-zA-Z]", format_spec):
                                    format_spec = format_spec.replace(":", ":.", 1)
                        elif isinstance(value.format_spec, ast.JoinedStr):
                            # Complex format spec (another f-string)
                            # Recursively convert the format spec
                            format_spec_call = self.concac(value.format_spec)  # Use concac instead of fm
                            
                            # Extract the format string from the recursive call
                            if isinstance(format_spec_call.func.value, ast.Constant):
                                nested_format = format_spec_call.func.value.value
                            else:
                                # Fallback if the format string isn't a constant
                                nested_format = ""
                            
                            format_spec = ":" + nested_format
                            # Add format spec conversion arguments before the main value
                            args.extend(format_spec_call.args)
                    
                    # Create the format placeholder
                    format_parts.append("{" + conversion + format_spec + "}")
                    
                    # Add the argument
                    args.append(value.value)
            
            # Join the format parts
            format_string = ''.join(format_parts)
            
            # If obfuscation is needed, apply it here (assuming Ast_obf().obfct is valid)
            try:
                format_string = ast.unparse(Ast_obf().obfct(format_string))
            except (NameError, AttributeError):
                # If Ast_obf isn't defined or doesn't have obfct method, use the string as is
                pass
            return ast.Call(
                func=ast.Attribute(
                    # value=ast.Constant(value=format_string),
                    value=ast.Name(id=format_string, ctx=ast.Load()),
                    attr="format",
                    ctx=ast.Load(),
                ),
                args=args,
                keywords=[],
            )


        def obfuscate(self, node):
            # if not self.spam:
            Logging.event('Obfuscate string, bytes, and lists!')
            for i in ast.walk(node):
                if isinstance(i, (ast.Global, ast.Nonlocal)):
                    continue
                for f, v in ast.iter_fields(i):
                    # Handle fields that contain lists of nodes
                    if isinstance(v, list):
                        ar = []
                        for j in v:
                            try:
                                if isinstance(j, ast.Constant):
                                    # Handle string constants
                                    if isinstance(j.value, str):
                                        string_type = (
                                            'r' if j.value.startswith('r')
                                            else 'fr' if j.value.startswith('fr')
                                            else ''
                                        )
                                        ar.append(Ast_obf().obfct(j.value, string_type))
                                        continue
                                        
                                    # Handle integer constants
                                    if isinstance(j.value, int) and not isinstance(j.value, bool):
                                        ar.append(self.obfint(j.value))
                                        continue
                                        
                                    # Handle float constants - uncomment if needed
                                    if isinstance(j.value, float) and self.mode > 1:
                                        ar.append(self.obffloat(j.value))
                                        continue
                                        
                                    # Default case: preserve the constant
                                    ar.append(j)
                                    continue
                                    
                                # Handle f-strings (JoinedStr nodes)
                                elif isinstance(j, ast.JoinedStr):
                                    ar.append(self.concac(j))
                                    continue
                                    
                                # Any other AST node: keep as is
                                elif isinstance(j, ast.AST):
                                    ar.append(j)
                                    continue
                                    
                                # Non-AST items in the list (shouldn't normally happen)
                                ar.append(j)
                                
                            except Exception as e:
                                Logging.warning(f"Error processing node {type(j).__name__}: {e}")
                                # Preserve the original node on error
                                ar.append(j)
                                
                        # Update the field with our processed list
                        try:
                            setattr(i, f, ar)
                        except (TypeError, AttributeError) as e:
                            Logging.error(f"Cannot set attribute {f} on {type(i).__name__}: {e}")
                            
                    # Handle single value fields (non-list)
                    else:
                        try:
                            # Handle string constants
                            if isinstance(v, ast.Constant) and isinstance(v.value, str):
                                string_type = (
                                    'r' if v.value.startswith('r')
                                    else 'fr' if v.value.startswith('fr')
                                    else ''
                                )
                                setattr(i, f, Ast_obf().obfct(v.value, string_type))
                            
                            # Handle integer constants
                            elif isinstance(v, ast.Constant) and isinstance(v.value, int) and not isinstance(v.value, bool):
                                setattr(i, f, self.obfint(v.value))
                            
                            # Handle float constants
                            elif isinstance(v, ast.Constant) and isinstance(v.value, float):
                                setattr(i, f, self.obffloat(v.value))
                            
                            # Handle f-strings
                            elif isinstance(v, ast.JoinedStr):
                                setattr(i, f, self.concac(v))
                            
                        except Exception as e:
                            Logging.warning(f"Error processing field {f} on {type(i).__name__}: {e}")
                            # Field remains unchanged on error


        def __call__(self, code: str) -> str:
            tree = ast.parse(code)
            self.obfuscate(tree)
            if self.spam:
                tbd = Ast_obf().trycatch(tree.body, 2)
                return ast.unparse(tbd)
            return ast.unparse(tree)
class Logging:
    """Lớp hỗ trợ ghi log với các cấp độ khác nhau, hiển thị chuyên nghiệp hơn với bảy sắc cầu vồng."""
    
    colorama.init(autoreset=True)  # Tự động reset màu sau mỗi log
    
    @staticmethod
    def _log(level: str, gradient, msg: str) -> None:
        """Hàm nội bộ để chuẩn hóa định dạng log."""
        log_text = f"{msg}"
        
        print(f" {Col.Symbol(level, light, dark)} "+Colorate.Horizontal(gradient, log_text))

    @staticmethod
    def event(msg: str) -> None:
        Logging._log("EVENT", Colors.red_to_white, msg)

    @staticmethod
    def info(msg: str) -> None:
        Logging._log("INFO", Colors.white_to_red, msg)

    @staticmethod
    def success(msg: str) -> None:
        Logging._log("SUCCESS", Colors.cyan_to_green, msg)

    @staticmethod
    def warning(msg: str) -> None:
        """Ghi log cảnh báo - Gradient Lục-Xanh."""
        Logging._log("WARNING", Colors.yellow_to_red, msg)

    @staticmethod
    def notice(msg: str) -> None:
        """Ghi log thông báo quan trọng - Gradient Xanh-Chàm."""
        Logging._log("NOTICE", Colors.blue_to_purple, msg)

    @staticmethod
    def debug(msg: str) -> None:
        """Ghi log debug - Gradient Chàm-Tím."""
        Logging._log("DEBUG", Colors.purple_to_red, msg)

    @staticmethod
    def error(msg: str) -> None:
        """Ghi log lỗi nghiêm trọng - Gradient Đỏ-Tím."""
        Logging._log("ERROR", Colors.red_to_purple, msg)

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

        # Convert and store global variables
        self.args.protect = self.args.protect.lower() == 'true'
        globals()['mode'] = int(self.args.mode)
        globals()['protect'] = self.args.protect
        globals()['type_run'] = self.args.type.upper()

class vdt(ast.NodeTransformer):
    """
    AST transformer that identifies different forms of variable declarations
    and converts between them while preserving functionality.
    
    Handles conversion between:
    - globals()['var'] = value  ⟷  global var; var = value
    - locals()['var'] = value   ⟷  var = value
    - vars()['var'] = value     ⟷  var = value (in current scope)
    """
    
    def __init__(self):
        self.modified = False
        # Track global declarations to avoid duplicates
        self.global_vars = set()
        # Track current function scope
        self.current_function = None
        
    def visit_FunctionDef(self, node: ast.FunctionDef) -> ast.FunctionDef:
        """Track function scope when entering a function definition"""
        old_function = self.current_function
        old_globals = self.global_vars.copy()
        self.current_function = node
        self.global_vars = set()  # Reset globals for this function scope
        
        # Process the function body
        node = self.generic_visit(node)
        
        # If we found globals() references in expressions, add global statements
        if self.global_vars and self.current_function:
            # Create a global statement for all identified global vars
            global_stmt = ast.Global(names=list(self.global_vars))
            ast.copy_location(global_stmt, node.body[0] if node.body else node)
            
            # Insert at the beginning of the function body
            node.body.insert(0, global_stmt)
            self.modified = True
        
        # Restore previous function context
        self.current_function = old_function
        self.global_vars = old_globals
        return node
    
    def visit_Global(self, node: ast.Global) -> ast.Global:
        """Track global declarations"""
        for name in node.names:
            self.global_vars.add(name)
        return node
    
    def visit_Assign(self, node: ast.Assign) -> Union[ast.Assign, List[ast.AST]]:
        """
        Identifies assignments like:
        - globals()['var'] = value -> convert to: global var; var = value
        - vars()['var'] = value -> convert to: var = value
        - locals()['var'] = value -> convert to: var = value
        - complex_var = something + globals()['var'] -> complex_var = something + var
        """
        # First, transform the value part to handle cases where globals() is used in expressions
        node.value = self.visit_globals_in_expr(node.value)
        
        # Check if this is a potential dictionary assignment to a namespace
        if len(node.targets) == 1 and isinstance(node.targets[0], ast.Subscript):
            subscript = node.targets[0]
            
            # Check if the value being subscripted is a call to globals(), vars(), or locals()
            if (isinstance(subscript.value, ast.Call) and 
                isinstance(subscript.value.func, ast.Name) and
                subscript.value.func.id in ('globals', 'vars', 'locals')):
                
                # Check if the index is a string literal
                if (isinstance(subscript.slice, ast.Constant) and
                    isinstance(subscript.slice.value, str)):
                    
                    var_name = subscript.slice.value
                    namespace_func = subscript.value.func.id
                    
                    # Convert dictionary-style assignment to direct assignment
                    # For globals(), we need to add a global statement if we're in a function
                    if namespace_func == 'globals' and self.current_function and var_name not in self.global_vars:
                        # Create a global statement
                        global_stmt = ast.Global(names=[var_name])
                        ast.copy_location(global_stmt, node)
                        
                        # Create the regular assignment
                        assign_stmt = ast.Assign(
                            targets=[ast.Name(id=var_name, ctx=ast.Store())],
                            value=node.value
                        )
                        ast.copy_location(assign_stmt, node)
                        
                        # Add to tracked globals
                        self.global_vars.add(var_name)
                        self.modified = True
                        
                        # Return both statements
                        return [global_stmt, assign_stmt]
                    else:
                        # For locals() and vars(), just convert to regular assignment
                        # For globals() outside a function, same treatment
                        assign_stmt = ast.Assign(
                            targets=[ast.Name(id=var_name, ctx=ast.Store())],
                            value=node.value
                        )
                        ast.copy_location(assign_stmt, node)
                        self.modified = True
                        
                        # Add a comment node
                        comment = ast.Expr(
                            value=ast.Constant(
                                value=f"# Converted from {namespace_func}()['{var_name}']",
                                kind=None
                            )
                        )
                        
                        return [comment, assign_stmt]
        
        # For all other cases, return the node unchanged
        return node
        
    def visit_globals_in_expr(self, node: ast.expr) -> ast.expr:
        """
        Converts globals()['var'] references in expressions to direct variable references.
        For example: a = b + globals()['c'] -> a = b + c
        """
        if isinstance(node, ast.BinOp):
            # Recursively process both sides of the binary operation
            node.left = self.visit_globals_in_expr(node.left)
            node.right = self.visit_globals_in_expr(node.right)
            return node
            
        elif isinstance(node, ast.UnaryOp):
            # Process the operand of unary operations
            node.operand = self.visit_globals_in_expr(node.operand)
            return node
            
        elif isinstance(node, ast.Compare):
            # Process the left side and all comparators
            node.left = self.visit_globals_in_expr(node.left)
            node.comparators = [self.visit_globals_in_expr(comp) for comp in node.comparators]
            return node
            
        elif isinstance(node, ast.Call):
            # Process function arguments
            node.args = [self.visit_globals_in_expr(arg) for arg in node.args]
            node.keywords = [
                ast.keyword(arg=kw.arg, value=self.visit_globals_in_expr(kw.value))
                for kw in node.keywords
            ]
            return node
            
        elif isinstance(node, ast.Subscript) and isinstance(node.value, ast.Call):
            # Check if this is a globals(), locals(), or vars() dictionary access
            if (isinstance(node.value.func, ast.Name) and
                node.value.func.id in ('globals', 'vars', 'locals') and
                isinstance(node.slice, ast.Constant) and
                isinstance(node.slice.value, str)):
                
                var_name = node.slice.value
                namespace_func = node.value.func.id
                
                # If we're in a function and this is a globals() reference, add to tracked globals
                if namespace_func == 'globals' and self.current_function and var_name not in self.global_vars:
                    # We'll need to add a global statement for this variable
                    # We'll do this when we get back to the function definition
                    self.global_vars.add(var_name)
                
                # Replace with a direct name reference
                name_node = ast.Name(id=var_name, ctx=ast.Load())
                ast.copy_location(name_node, node)
                self.modified = True
                return name_node
                
        # For all other cases, return the node unchanged
        return node
    
def ymt(code: str, mode: str = "equivalents") -> str:
    """
    Transform Python code to convert between different forms of variable declarations.
    
    Args:
        code: The Python code to transform
        mode: The transformation mode
              - "equivalents": Convert dictionary-style to standard declarations
        
    Returns:
        The transformed code
    """
    
    tree = ast.parse(code)
    transformer = vdt()
    transformed_tree = transformer.visit(tree)
    ast.fix_missing_locations(transformed_tree)
    if transformer.modified:
        return ast.unparse(transformed_tree)
    else:
        return code
    
def clean_try_except(code_str):
    try:
        original_ast = ast.parse(code_str)
        try_body = original_ast.body
        
        # Handler for general exceptions
        print_call = ast.Expr(
            value=ast.Call(
                func=ast.Name(id='print', ctx=ast.Load()),
                args=[ast.Name(id='TrinhDepTraiTrinhDepTraiTrinhDepTraiTrinhDepTraiTrinhDepTraiTrinhDepTraiTrinhDepTraiTrinhDepTraiTrinhDepTraiTrinhDepTraiTrinhDepTraiTrinhDepTraiTrinhDepTrai', ctx=ast.Load()),],
                keywords=[]
            )
        )
        
        exception_handler = ast.ExceptHandler(
            type=ast.Name(id='Exception', ctx=ast.Load()),
            name='TrinhDepTraiTrinhDepTraiTrinhDepTraiTrinhDepTraiTrinhDepTraiTrinhDepTraiTrinhDepTraiTrinhDepTraiTrinhDepTraiTrinhDepTraiTrinhDepTraiTrinhDepTraiTrinhDepTrai',
            body=[print_call]
        )
        
        # Handler for KeyboardInterrupt
        print_exiting_call = ast.Expr(
            value=ast.Call(
                func=ast.Name(id='print', ctx=ast.Load()),
                args=[ast.Constant(value='\n\nExiting...')],
                keywords=[]
            )
        )
        
        # Add exit call
        exit_call = ast.Expr(
            value=ast.Call(
                func=ast.Name(id='exit', ctx=ast.Load()),
                args=[],
                keywords=[]
            )
        )
        
        keyboard_interrupt_handler = ast.ExceptHandler(
            type=ast.Name(id='KeyboardInterrupt', ctx=ast.Load()),
            name=None,
            body=[print_exiting_call, exit_call]
        )
        
        try_except = ast.Try(
            body=try_body,
            handlers=[keyboard_interrupt_handler, exception_handler],  # Order matters: KeyboardInterrupt first
            orelse=[],
            finalbody=[]
        )
        
        new_module = ast.Module(body=[try_except], type_ignores=[])
        
        ast.fix_missing_locations(new_module)
        
        return ast.unparse(new_module)
    except SyntaxError as e:
        return f"# Invalid code: {str(e)}"

def main(): 
    global banner
    print(' ' *len('>> Loading...'), end='\r')
    banner = Add.Add(banner, sakura, center=True)
    print(Colorate.Diagonal(Colors.DynamicMIX((sakura_, dark)), banner))
    args = ParseArgs().args
    print(' '+'- '*30)
    if not args.file:
        file = input(stage(f"Drag the file you want to obfuscate {dark}-> {Col.reset}", "?", col2 = bsakura_)).replace('"','').replace("'","")
        print(' '+'- '*30)
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
        input(f" {Col.Symbol('!', light, dark)} {Col.light_red}Invalid file or code!{Col.reset}")
        exit()

    Logging.event('Cleaning Source Code')
    code = clean_try_except(ymt(code))
    code = hard_code+code
    Logging.event('Adding Anti PYCDC')
    build_anti_pycdc()
    Logging.event('Adding Vars')
    build_var()
    if int(args.mode) != 1:
        code = ast.unparse(Ast_obf().rn_func(ast.parse(code), "print",__print))
        code = ast.unparse(Ast_obf().rn_func(ast.parse(code), "input",__input))
    if int(args.mode) == 2:
        open(args.output[:-3]+'-var.py', 'w', encoding='utf-8').write(Methods.obf_vars(code_))
        operations = [
            Methods.obf_vars,
            Ast_obf().spam,
            Ast_obf().spam,
            Methods.obf_builtins,
            Methods.obf_strings(args.mode, True),
            Compile.Obfuscate,
            Methods.last_obf_builtins,
        ]
    else:
        operations = [
            Ast_obf().spam,
            Ast_obf().spam,
            Methods.obf_builtins,
            Methods.obf_strings(args.mode, True),
            Compile.Obfuscate,
            Methods.last_obf_builtins,
        ]
    hacker = f"__TrinhNguyen0611__ = vars(globals()[{Pycloak().encode('__builtins__')}])\n"+pro

    st = time.time()
    for operation in operations:
        code = operation(code)
    with open(args.output, 'w', encoding='utf-8') as f:
        f.write("#!/bin/python3\n"+((((((code)))))))
        done = time.time() - st
        Logging.success(f'Wrote file {args.output}. Done in {round(done, 3)}s.')

main()
