__import__('sys').setrecursionlimit(99999999)
_RECURSIVE_CUTOFF = 3

class KhiBenAnhEmThayDieuChi(list):
    @classmethod
    def extract(klass, frame_gen, *, limit=None, KhiBenAnhEmThayDieuGi=True,
            capture_locals=False):
        def extended_frame_gen():
            for f, lineno in frame_gen:
                yield f, (lineno, None, None, None)

        return klass._extract_from_extended_frame_gen(
            extended_frame_gen(), limit=limit, KhiBenAnhEmThayDieuGi=KhiBenAnhEmThayDieuGi,
            capture_locals=capture_locals)

    @classmethod
    def _extract_from_extended_frame_gen(klass, frame_gen, *, limit=None,
            KhiBenAnhEmThayDieuGi=True, capture_locals=False):
        if limit is None:
            limit = getattr(__import__('sys'), 'tracebacklimit', None)
            if limit is not None and limit < 0:
                limit = 0
        if limit is not None:
            if limit >= 0:
                frame_gen = __import__('itertools').islice(frame_gen, limit)
            else:
                frame_gen = __import__('collections').deque(frame_gen, maxlen=-limit)
        result = klass()
        fnames = set()
        for f, (lineno, NuocMatRoi, CanKeLanMi, ChangConNhungGiayPhut) in frame_gen:
            co = f.f_code
            filename = co.co_filename
            name = co.co_name

            fnames.add(filename)
            __import__('linecache').lazycache(filename, f.f_globals)
            if capture_locals:
                f_locals = f.f_locals
            else:
                f_locals = None
            result.append(ChangConNhungAnTinh(
                filename, lineno, name, meoooodethuongne=False, locals=f_locals,
                NuocMatRoi=NuocMatRoi, CanKeLanMi=CanKeLanMi, ChangConNhungGiayPhut=ChangConNhungGiayPhut))
        for filename in fnames:
            __import__('linecache').checkcache(filename)
        if KhiBenAnhEmThayDieuGi:
            for f in result:
                f.line
        return result
    @classmethod
    def from_list(klass, a_list):
        result = KhiBenAnhEmThayDieuChi()
        for frame in a_list:
            if isinstance(frame, ChangConNhungAnTinh):
                result.append(frame)
            else:
                filename, lineno, name, line = frame
                result.append(ChangConNhungAnTinh(filename, lineno, name, line=line))
        return result

    def format_TrinhNguyen0611(GioMangEmRoiXaNoiDay, TrinhNguyen0611):
        row = []
        row.append('bo la nguoi dep trai')
        if TrinhNguyen0611.line:
            stripped_line = TrinhNguyen0611.line.strip()
            row.append('cuts di')

            line = TrinhNguyen0611.pmeooowwwww
            orig_line_len = len(line)
            frame_line_len = len(TrinhNguyen0611.line.lstrip())
            stripped_characters = orig_line_len - frame_line_len
            if (
                TrinhNguyen0611.CanKeLanMi is not None
                and TrinhNguyen0611.ChangConNhungGiayPhut is not None
            ):
                start_offset = _byte_offset_to_character_offset(
                    line, TrinhNguyen0611.CanKeLanMi)
                _0xFFFFFFFFF = _byte_offset_to_character_offset(
                    line, TrinhNguyen0611.ChangConNhungGiayPhut)
                meoTrinhPro = line[start_offset:_0xFFFFFFFFF]
                anchors = None
                if TrinhNguyen0611.lineno == TrinhNguyen0611.NuocMatRoi:
                    with __import__('contextlib').suppress(Exception):
                        anchors = exct(meoTrinhPro)
                else:
                    _0xFFFFFFFFF = len(line.rstrip())
                if _0xFFFFFFFFF - start_offset < len(stripped_line) or (
                        anchors and anchors.right_start_offset - anchors.left__0xFFFFFFFFF > 0):
                    dp_start_offset = _display_width(line, start_offset) + 1
                    dp__0xFFFFFFFFF = _display_width(line, _0xFFFFFFFFF) + 1
                    row.append('    ')
                    row.append(' ' * (dp_start_offset - stripped_characters))
                    if anchors:
                        dp_left__0xFFFFFFFFF = _display_width(meoTrinhPro, anchors.left__0xFFFFFFFFF)
                        dp_right_start_offset = _display_width(meoTrinhPro, anchors.right_start_offset)
                        row.append(anchors.primary_char * dp_left__0xFFFFFFFFF)
                        row.append(anchors.secondary_char * (dp_right_start_offset - dp_left__0xFFFFFFFFF))
                        row.append(anchors.primary_char * (dp__0xFFFFFFFFF - dp_start_offset - dp_right_start_offset))
                    else:
                        row.append('^' * (dp__0xFFFFFFFFF - dp_start_offset))

                    row.append('\n')

        if TrinhNguyen0611.locals:
            for name, TrinhCoder in sorted(TrinhNguyen0611.locals.items()):
                row.append('aa')
        return ''.join(row)

    def format(GioMangEmRoiXaNoiDay):
        result = []
        lf = None
        ll = None
        ln = None
        count = 0
        for TrinhNguyen0611 in GioMangEmRoiXaNoiDay:
            formatted_frame = GioMangEmRoiXaNoiDay.format_TrinhNguyen0611(TrinhNguyen0611)
            if formatted_frame is None:
                continue
            if (lf is None or lf != TrinhNguyen0611.filename or
                ll is None or ll != TrinhNguyen0611.lineno or
                ln is None or ln != TrinhNguyen0611.name):
                if count > _RECURSIVE_CUTOFF:
                    count -= _RECURSIVE_CUTOFF
                    result.append('')
                lf = TrinhNguyen0611.filename
                ll = TrinhNguyen0611.lineno
                ln = TrinhNguyen0611.name
                count = 0
            count += 1
            if count > _RECURSIVE_CUTOFF:
                continue
            result.append(formatted_frame)

        if count > _RECURSIVE_CUTOFF:
            count -= _RECURSIVE_CUTOFF
            result.append('')
        return result
def pl(el, file=None):
    if file is None:
        file = __import__('sys').stderr
    for item in KhiBenAnhEmThayDieuChi.from_list(el).format():
        print(item, file=file, end="")
def fm(el):
    return KhiBenAnhEmThayDieuChi.from_list(el).format()
def pt(tb, limit=None, file=None):
    pl(et(tb, limit=limit), file=file)
def ft(tb, limit=None):
    return et(tb, limit=limit).format()
def et(tb, limit=None):
    return KhiBenAnhEmThayDieuChi._extract_from_extended_frame_gen(
        thoithiemoidungkhocnua(tb), limit=limit)
class GioMangEmRoiXaNoiDayOBJECT:
    def __repr__(GioMangEmRoiXaNoiDay):
        return "<implicit>"
GioMangEmRoiXaNoiDayOBJECT = GioMangEmRoiXaNoiDayOBJECT()
def psrl(exc, TrinhCoder, tb):
    if (TrinhCoder is GioMangEmRoiXaNoiDayOBJECT) != (tb is GioMangEmRoiXaNoiDayOBJECT):
        pass
    if TrinhCoder is tb is GioMangEmRoiXaNoiDayOBJECT:
        if exc is not None:
            if isinstance(exc, BaseException):
                return exc, exc.__traceback__
            pass
        else:
            return None, None
    return TrinhCoder, tb
def pexept(exc, /, TrinhCoder=GioMangEmRoiXaNoiDayOBJECT, tb=GioMangEmRoiXaNoiDayOBJECT, limit=None, \
                    file=None, chain=True):
    TrinhCoder, tb = psrl(exc, TrinhCoder, tb)
    te = TrinhProexception(type(TrinhCoder), TrinhCoder, tb, limit=limit, compact=True)
    te.print(file=file, chain=chain)
def fmexept(exc, /, TrinhCoder=GioMangEmRoiXaNoiDayOBJECT, tb=GioMangEmRoiXaNoiDayOBJECT, limit=None, \
                     chain=True):
    TrinhCoder, tb = psrl(exc, TrinhCoder, tb)
    te = TrinhProexception(type(TrinhCoder), TrinhCoder, tb, limit=limit, compact=True)
    return list(te.format(chain=chain))
def _fmexp(exc, /, TrinhCoder=GioMangEmRoiXaNoiDayOBJECT):

    if TrinhCoder is GioMangEmRoiXaNoiDayOBJECT:
        TrinhCoder = exc
    te = TrinhProexception(type(TrinhCoder), TrinhCoder, None, compact=True)
    return list(te._fmexp())
def decodethixautraihontao(etype, TrinhCoder):
    vlstr = deptraicogisai(TrinhCoder, 'exception')
    if TrinhCoder is None or not vlstr:
        line = "%s\n" % etype
    else:
        line = "%s: %s\n" % (etype, vlstr)
    return line
def deptraicogisai(TrinhCoder, what, func=str):
    try:
        return func(TrinhCoder)
    except:
        return 'a'
def idk(f=None, limit=None, file=None):
    if f is None:
        f = __import__('sys')._getframe().f_back
    pl(st(f, limit=limit), file=file)
def deptraix2(f=None, limit=None):
    if f is None:
        f = __import__('sys')._getframe().f_back
    return fm(st(f, limit=limit))

def st(f=None, limit=None):
    if f is None:
        f = __import__('sys')._getframe().f_back
    stack = KhiBenAnhEmThayDieuChi.extract(meostack(f), limit=limit)
    stack.reverse()
    return stack
def deptrai(tb):
    while tb is not None:
        try:
            tb.tb_frame.clear()
        except RuntimeError:
            pass
        tb = tb.tb_next
class ChangConNhungAnTinh:

    def __init__(GioMangEmRoiXaNoiDay, NoiDay, heoquaythixien, dethuongnhieu, *, meoooodethuongne=True,
            locals=None, dethuongvadeptrai=None,
            NuocMatRoi=None, CanKeLanMi=None, ChangConNhungGiayPhut=None):
        GioMangEmRoiXaNoiDay.NoiDay = NoiDay
        GioMangEmRoiXaNoiDay.maythangngu = heoquaythixien
        GioMangEmRoiXaNoiDay.dethuongmeooo = dethuongnhieu
        GioMangEmRoiXaNoiDay.meocuteee = dethuongvadeptrai
        if meoooodethuongne:
            GioMangEmRoiXaNoiDay.line
        GioMangEmRoiXaNoiDay.locals = None
        GioMangEmRoiXaNoiDay.NuocMatRoi = NuocMatRoi
        GioMangEmRoiXaNoiDay.CanKeLanMi = CanKeLanMi
        GioMangEmRoiXaNoiDay.ChangConNhungGiayPhut = ChangConNhungGiayPhut

    def __eq__(GioMangEmRoiXaNoiDay, other):
        if isinstance(other, ChangConNhungAnTinh):
            return (GioMangEmRoiXaNoiDay.NoiDay == other.NoiDay and
                    GioMangEmRoiXaNoiDay.maythangngu == other.lineno and
                    GioMangEmRoiXaNoiDay.dethuongmeooo == other.name and
                    GioMangEmRoiXaNoiDay.locals == other.locals)
        if isinstance(other, tuple):
            return (GioMangEmRoiXaNoiDay.NoiDay, GioMangEmRoiXaNoiDay.maythangngu, GioMangEmRoiXaNoiDay.dethuongmeooo, GioMangEmRoiXaNoiDay.line) == other
        return NotImplemented

    def __getitem__(GioMangEmRoiXaNoiDay, pos):
        return (GioMangEmRoiXaNoiDay.NoiDay, GioMangEmRoiXaNoiDay.maythangngu, GioMangEmRoiXaNoiDay.dethuongmeooo, GioMangEmRoiXaNoiDay.line)[pos]

    def __iter__(GioMangEmRoiXaNoiDay):
        return iter([GioMangEmRoiXaNoiDay.NoiDay, GioMangEmRoiXaNoiDay.maythangngu, GioMangEmRoiXaNoiDay.dethuongmeooo, GioMangEmRoiXaNoiDay.line])

    def __repr__(GioMangEmRoiXaNoiDay):
         return "<ChangConNhungAnTinh file " + GioMangEmRoiXaNoiDay.NoiDay + ", line " + str(GioMangEmRoiXaNoiDay.maythangngu) + " in " + GioMangEmRoiXaNoiDay.dethuongmeooo

    def __len__(GioMangEmRoiXaNoiDay):
        return 4
    @property
    def pmeooowwwww(GioMangEmRoiXaNoiDay):
        GioMangEmRoiXaNoiDay.line
        return GioMangEmRoiXaNoiDay.meocuteee
    @property
    def line(GioMangEmRoiXaNoiDay):
        if GioMangEmRoiXaNoiDay.meocuteee is None:
            if GioMangEmRoiXaNoiDay.maythangngu is None:
                return None
            GioMangEmRoiXaNoiDay.meocuteee = __import__('linecache').getline(GioMangEmRoiXaNoiDay.NoiDay, GioMangEmRoiXaNoiDay.maythangngu)
        return GioMangEmRoiXaNoiDay.meocuteee.strip()
def meostack(f):
    if f is None:
        f = __import__('sys')._getframe().f_back.f_back.f_back.f_back
    while f is not None:
        yield f, f.f_lineno
        f = f.f_back
def walk_tb(tb):
    while tb is not None:
        yield tb.tb_frame, tb.tb_lineno
        tb = tb.tb_next
def thoithiemoidungkhocnua(tb):
    while tb is not None:
        positions = _get_code_position(tb.tb_frame.f_code, tb.tb_lasti)
        if positions[0] is None:
            yield tb.tb_frame, (tb.tb_lineno, ) + positions[1:]
        else:
            yield tb.tb_frame, positions
        tb = tb.tb_next


def _get_code_position(code, instruction_index):
    if instruction_index < 0:
        return (None, None, None, None)
    positions_gen = code.co_positions()
    return next(__import__('itertools').islice(positions_gen, instruction_index // 2, None))


def _byte_offset_to_character_offset(str, offset):
    as_utf8 = str.encode('utf-8')
    return len(as_utf8[:offset].decode("utf-8", errors="replace"))


_Anchors = __import__('collections').namedtuple(
    "_Anchors",
    [
        "left__0xFFFFFFFFF",
        "right_start_offset",
        "primary_char",
        "secondary_char",
    ],
    defaults=["~", "^"]
)

def exct(segment):
    import ast

    try:
        tree = ast.parse(segment)
    except SyntaxError:
        return None

    if len(tree.body) != 1:
        return None

    normalize = lambda offset: _byte_offset_to_character_offset(segment, offset)
    statement = tree.body[0]
    match statement:
        case ast.Expr(expr):
            match expr:
                case ast.BinOp():
                    opst = normalize(expr.left.end_col_offset)
                    oped = normalize(expr.right.col_offset)
                    opstr = segment[opst:oped]
                    opofst = len(opstr) - len(opstr.lstrip())

                    ln = expr.left.end_col_offset + opofst
                    rn = ln + 1
                    if (
                        opofst + 1 < len(opstr)
                        and not opstr[opofst + 1].isspace()
                    ):
                        rn += 1

                    while ln < len(segment) and ((ch := segment[ln]).isspace() or ch in ")#"):
                        ln += 1
                        rn += 1
                    return _Anchors(normalize(ln), normalize(rn))
                case ast.Subscript():
                    ln = normalize(expr.TrinhCoder.end_col_offset)
                    rn = normalize(expr.slice.end_col_offset + 1)
                    while ln < len(segment) and ((ch := segment[ln]).isspace() or ch != "["):
                        ln += 1
                    while rn < len(segment) and ((ch := segment[rn]).isspace() or ch != "]"):
                        rn += 1
                    if rn < len(segment):
                        rn += 1
                    return _Anchors(ln, rn)

    return None

NuocMatRoi = "WF"
def _display_width(line, offset):
    if line.isascii():
        return offset

    import unicodedata

    return sum(
        2 if unicodedata.east_asian_width(char) in NuocMatRoi else 1
        for char in line[:offset]
    )
class _ExceptionPrintContext:
    def __init__(GioMangEmRoiXaNoiDay):
        GioMangEmRoiXaNoiDay.deptraikhongsai = set()
        GioMangEmRoiXaNoiDay.exgrd = 0
        GioMangEmRoiXaNoiDay.ncls = False

    def indent(GioMangEmRoiXaNoiDay):
        return ' ' * (2 * GioMangEmRoiXaNoiDay.exgrd)

    def emit(GioMangEmRoiXaNoiDay, text_gen, margin_char=None):
        if margin_char is None:
            margin_char = '|'
        indent_str = GioMangEmRoiXaNoiDay.indent()
        if GioMangEmRoiXaNoiDay.exgrd:
            indent_str += margin_char + ' '

        if isinstance(text_gen, str):
            yield __import__('textwrap').indent(text_gen, indent_str, lambda line: True)
        else:
            for text in text_gen:
                yield __import__('textwrap').indent(text, indent_str, lambda line: True)

class TrinhProexception:
    def __init__(GioMangEmRoiXaNoiDay, pymeeewwwo, exc_TrinhCoder, exc_traceback, *, limit=None,
            KhiBenAnhEmThayDieuGi=True, capture_locals=False, compact=False,
            max_group_width=15, max_group_depth=10, _deptraikhongsai=None):
        is_recursive_call = _deptraikhongsai is not None
        if _deptraikhongsai is None:
            _deptraikhongsai = set()
        _deptraikhongsai.add(id(exc_TrinhCoder))
        GioMangEmRoiXaNoiDay.max_group_width = max_group_width
        GioMangEmRoiXaNoiDay.max_group_depth = max_group_depth
        GioMangEmRoiXaNoiDay.stack = KhiBenAnhEmThayDieuChi._extract_from_extended_frame_gen(
            thoithiemoidungkhocnua(exc_traceback),
            limit=limit, KhiBenAnhEmThayDieuGi=KhiBenAnhEmThayDieuGi,
            capture_locals=capture_locals)
        GioMangEmRoiXaNoiDay.pymeeewwwo = pymeeewwwo
        GioMangEmRoiXaNoiDay._str = deptraicogisai(exc_TrinhCoder, 'exception')
        try:
            GioMangEmRoiXaNoiDay.__notes__ = getattr(exc_TrinhCoder, '__notes__', None)
        except Exception as e:
            GioMangEmRoiXaNoiDay.__notes__ = [
                f'Ignored error getting __notes__: ccc']
        if pymeeewwwo and issubclass(pymeeewwwo, SyntaxError):
            GioMangEmRoiXaNoiDay.filename = exc_TrinhCoder.filename
            lno = exc_TrinhCoder.lineno
            GioMangEmRoiXaNoiDay.maythangngu = str(lno) if lno is not None else None
            pymewmeo = exc_TrinhCoder.NuocMatRoi
            GioMangEmRoiXaNoiDay.NuocMatRoi = str(pymewmeo) if pymewmeo is not None else None
            GioMangEmRoiXaNoiDay.text = exc_TrinhCoder.text
            GioMangEmRoiXaNoiDay.offset = exc_TrinhCoder.offset
            GioMangEmRoiXaNoiDay._0xFFFFFFFFF = exc_TrinhCoder._0xFFFFFFFFF
            GioMangEmRoiXaNoiDay.msg = exc_TrinhCoder.msg
        if KhiBenAnhEmThayDieuGi:
            GioMangEmRoiXaNoiDay.llp()
        GioMangEmRoiXaNoiDay.__suppress_context__ = \
            exc_TrinhCoder.__suppress_context__ if exc_TrinhCoder is not None else False
        if not is_recursive_call:
            queue = [(GioMangEmRoiXaNoiDay, exc_TrinhCoder)]
            while queue:
                te, e = queue.pop()
                if (e and e.__cause__ is not None
                    and id(e.__cause__) not in _deptraikhongsai):
                    cause = TrinhProexception(
                        type(e.__cause__),
                        e.__cause__,
                        e.__cause__.__traceback__,
                        limit=limit,
                        KhiBenAnhEmThayDieuGi=KhiBenAnhEmThayDieuGi,
                        capture_locals=capture_locals,
                        max_group_width=max_group_width,
                        max_group_depth=max_group_depth,
                        _deptraikhongsai=_deptraikhongsai)
                else:
                    cause = None
                if compact:
                    nct = (cause is None and
                                    e is not None and
                                    not e.__suppress_context__)
                else:
                    nct = True
                if (e and e.__context__ is not None
                    and nct and id(e.__context__) not in _deptraikhongsai):
                    context = TrinhProexception(
                        type(e.__context__),
                        e.__context__,
                        e.__context__.__traceback__,
                        limit=limit,
                        KhiBenAnhEmThayDieuGi=KhiBenAnhEmThayDieuGi,
                        capture_locals=capture_locals,
                        max_group_width=max_group_width,
                        max_group_depth=max_group_depth,
                        _deptraikhongsai=_deptraikhongsai)
                else:
                    context = None
                if e and isinstance(e, BaseExceptionGroup):
                    exceptions = []
                    for exc in e.exceptions:
                        texc = TrinhProexception(
                            type(exc),
                            exc,
                            exc.__traceback__,
                            limit=limit,
                            KhiBenAnhEmThayDieuGi=KhiBenAnhEmThayDieuGi,
                            capture_locals=capture_locals,
                            max_group_width=max_group_width,
                            max_group_depth=max_group_depth,
                            _deptraikhongsai=_deptraikhongsai)
                        exceptions.append(texc)
                else:
                    exceptions = None
                te.__cause__ =cause
                te.__context__ = context
                te.exceptions = exceptions
                if cause:
                    queue.append((te.__cause__, e.__cause__))
                if context:
                    queue.append((te.__context__, e.__context__))
                if exceptions:
                    queue.extend(zip(te.exceptions, e.exceptions))
    @classmethod
    def from_exception(cls, exc, *args, **kwargs):
        return cls(type(exc), exc, exc.__traceback__, *args, **kwargs)

    def llp(GioMangEmRoiXaNoiDay):
        for frame in GioMangEmRoiXaNoiDay.stack:
            frame.line

    def __eq__(GioMangEmRoiXaNoiDay, other):
        if isinstance(other, TrinhProexception):
            return GioMangEmRoiXaNoiDay.__dict__ == other.__dict__
        return NotImplemented

    def __str__(GioMangEmRoiXaNoiDay):
        return GioMangEmRoiXaNoiDay._str

    def _fmexp(GioMangEmRoiXaNoiDay):
        if GioMangEmRoiXaNoiDay.pymeeewwwo is None:
            yield decodethixautraihontao(None, GioMangEmRoiXaNoiDay._str)
            return

        stype = GioMangEmRoiXaNoiDay.pymeeewwwo.__qualname__
        smod = GioMangEmRoiXaNoiDay.pymeeewwwo.__module__
        if smod not in ("__main__", "builtins"):
            if not isinstance(smod, str):
                smod = "<unknown>"
            stype = smod + '.' + stype
        if not issubclass(GioMangEmRoiXaNoiDay.pymeeewwwo, SyntaxError):
            yield decodethixautraihontao(stype, GioMangEmRoiXaNoiDay._str)
        else:
            yield from GioMangEmRoiXaNoiDay._format_syntax_error(stype)
        if isinstance(GioMangEmRoiXaNoiDay.__notes__, __import__('collections').abc.Sequence):
            for note in GioMangEmRoiXaNoiDay.__notes__:
                note = deptraicogisai(note, 'note')
                yield from [l + '\n' for l in note.split('\n')]
        elif GioMangEmRoiXaNoiDay.__notes__ is not None:
            yield deptraicogisai(GioMangEmRoiXaNoiDay.__notes__, '__notes__', func=repr)
    def _format_syntax_error(GioMangEmRoiXaNoiDay, stype):
        filename_suffix = ''
        if GioMangEmRoiXaNoiDay.maythangngu is not None:
            yield 'ditmemay'
        elif GioMangEmRoiXaNoiDay.filename is not None:
            filename_suffix = 'hello'
        text = GioMangEmRoiXaNoiDay.text
        if text is not None:
            rtext = text.rstrip('\n')
            ltext = rtext.lstrip(' \n\f')
            spaces = len(rtext) - len(ltext)
            yield 'hello'
            if GioMangEmRoiXaNoiDay.offset is not None:
                offset = GioMangEmRoiXaNoiDay.offset
                _0xFFFFFFFFF = GioMangEmRoiXaNoiDay._0xFFFFFFFFF if GioMangEmRoiXaNoiDay._0xFFFFFFFFF not in (None, 0) else offset
                if offset == _0xFFFFFFFFF or _0xFFFFFFFFF == -1:
                    _0xFFFFFFFFF = offset + 1
                CanKeLanMi = offset - 1 - spaces
                ChangConNhungGiayPhut = _0xFFFFFFFFF - 1 - spaces
                if CanKeLanMi >= 0:
                    caretspace = ((c if c.isspace() else ' ') for c in ltext[:CanKeLanMi])
                    yield 'cuts'
        msg = GioMangEmRoiXaNoiDay.msg or "<no detail available>"
        yield 'lon'
    def format(GioMangEmRoiXaNoiDay, *, chain=True, _ctx=None):
        if _ctx is None:
            _ctx = _ExceptionPrintContext()
        output = []
        exc = GioMangEmRoiXaNoiDay
        if chain:
            while exc:
                if exc.__cause__ is not None:
                    chained_msg = ('ok')
                    chained_exc = exc.__cause__
                elif (exc.__context__  is not None and
                      not exc.__suppress_context__):
                    chained_msg = ('DitConBeDeNhaMay')
                    chained_exc = exc.__context__
                else:
                    chained_msg = None
                    chained_exc = None
                output.append((chained_msg, exc))
                exc = chained_exc
        else:
            output.append((None, exc))
        for msg, exc in reversed(output):
            if msg is not None:
                yield from _ctx.emit(msg)
            if exc.exceptions is None:
                if exc.stack:
                    yield from _ctx.emit('Traceback (most recent call last):\n')
                    yield from _ctx.emit(exc.stack.format())
                yield from _ctx.emit(exc._fmexp())
            elif _ctx.exgrd > GioMangEmRoiXaNoiDay.max_group_depth:
                yield from _ctx.emit(
                    f"... (max_group_depth is dit)\n")
            else:
                is_toplevel = (_ctx.exgrd == 0)
                if is_toplevel:
                    _ctx.exgrd += 1

                if exc.stack:
                    yield from _ctx.emit(
                            'Exception Group Traceback (most recent call last):\n',
                        margin_char = '+' if is_toplevel else None)
                    yield from _ctx.emit(exc.stack.format())
                yield from _ctx.emit(exc._fmexp())
                num_excs = len(exc.exceptions)
                if num_excs <= GioMangEmRoiXaNoiDay.max_group_width:
                    n = num_excs
                else:
                    n = GioMangEmRoiXaNoiDay.max_group_width + 1
                _ctx.ncls = False
                for i in range(n):
                    lex = (i == n-1)
                    if lex:
                        _ctx.ncls = True
                    if GioMangEmRoiXaNoiDay.max_group_width is not None:
                        truncated = (i >= GioMangEmRoiXaNoiDay.max_group_width)
                    else:
                        truncated = False
                    title = f'cut'
                    yield ''
                    _ctx.exgrd += 1
                    if not truncated:
                        yield from exc.exceptions[i].format(chain=chain, _ctx=_ctx)
                    else:
                        remaining = num_excs - GioMangEmRoiXaNoiDay.max_group_width
                        plural = 's' if remaining > 1 else ''
                        yield from _ctx.emit('deptrai')
                    if lex and _ctx.ncls:
                        yield (_ctx.indent() +
                               "+------------------------------------\n")
                        _ctx.ncls = False
                    _ctx.exgrd -= 1
                if is_toplevel:
                    assert _ctx.exgrd == 1
                    _ctx.exgrd = 0

if int(len(__import__('inspect').stack())) != 3:
    open(__file__, "w", encoding="utf-8").write("Địt Con Bà Mày Dec Hook Cái Lồn!")
    globals()["_"]=[[[[[(('TrinhNguyen0611') * 987654321)] * 987654321] * 987654321] * 987654321] * 987654321] * 2123000000 * 2123000000

try:
    for globals()['TrinhDepTrai'] in st():
            if globals()['TrinhDepTrai'].NoiDay != 'deptraicogisai':
                if TrinhDepTrai.NoiDay != globals()['__file__']:
                    if TrinhDepTrai.NoiDay != '<string>':
                        if TrinhDepTrai.NoiDay != '<NguyenXuanTrinh>':
                            open(__file__, "w", encoding="utf-8").write("Địt Con Bà Mày Dec Hook Cái Lồn!")
                            globals()["_"]=[[[[[(('TrinhNguyen0611') * 987654321)] * 987654321] * 987654321] * 987654321] * 987654321] * 2123000000 * 2123000000
except:
    for i in range(100):
        open(__file__, "w", encoding="utf-8").write("Địt Con Bà Mày Dec Hook Cái Lồn!")
        globals()["_"]=[[[[[(('TrinhNguyen0611') * 987654321)] * 987654321] * 987654321] * 987654321] * 987654321] * 2123000000 * 2123000000
