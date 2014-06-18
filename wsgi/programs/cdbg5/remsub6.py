
import cherrypy

# 這是 REMSUB6 類別的定義
'''
# 在 application 中導入子模組
import programs.cdag5.remsub6 as cdag5_remsub6
# 加入 cdag5 模組下的 remsub6.py 且以子模組 remsub6 對應其 MAIN() 類別
root.cdag5.remsub6 = cdag5_remsub6.MAIN()

# 完成設定後, 可以利用
/cdag5/remsub6/assembly
# 呼叫 remsub6.py 中 MAIN 類別的 assembly 方法
'''
class MAIN(object):
    # 各組利用 index 引導隨後的程式執行
    @cherrypy.expose
    def index(self, *args, **kwargs):
        outstring = '''
這是 2014CDA 協同專案下的 cdag5 模組下的 nremsub6.py 檔案中的 MAIN 類別.<br /><br />
<!-- 這裡採用相對連結, 而非網址的絕對連結 (這一段為 html 註解) -->
<a href="assembly">執行  MAIN 類別中的 assembly 方法</a><br /><br />
請確定下列零件於 V:/home/lego/nremsub6 目錄中, 且開啟空白 Creo 組立檔案.<br />
<a href="https://copy.com/oEKNnJlWGTSV">lego_parts.7z</a><br />
'''
        return outstring

    @cherrypy.expose
    def assembly(self, *args, **kwargs):
        outstring = '''
<!DOCTYPE html> 
<html>
<head>
<meta http-equiv="content-type" content="text/html;charset=utf-8">
<script type="text/javascript" src="/static/weblink/examples/jscript/pfcUtils.js"></script>
</head>
<body>
</script><script language="JavaScript">
/*man2.py 完全利用函式呼叫進行組立*/
/*設計一個零件組立函式*/
// featID 為組立件第一個組立零件的編號
// inc 則為 part1 的組立順序編號, 第一個入組立檔編號為 featID+0
// part2 為外加的零件名稱
////////////////////////////////////////////////
// axis_plane_assembly 組立函式
////////////////////////////////////////////////
function axis_plane_assembly(session, assembly, transf, featID, inc, part2, axis1, plane1, axis2, plane2){
var descr = pfcCreate("pfcModelDescriptor").CreateFromFileName ("v:/home/lego/nremsub6/"+part2);
var componentModel = session.GetModelFromDescr(descr);
var componentModel = session.RetrieveModel(descr);
if (componentModel != void null)
{
    var asmcomp = assembly.AssembleComponent (componentModel, transf);
}
var ids = pfcCreate("intseq");
ids.Append(featID+inc);
var subPath = pfcCreate("MpfcAssembly").CreateComponentPath(assembly, ids);
subassembly = subPath.Leaf;
var asmDatums = new Array(axis1, plane1);
var compDatums = new Array(axis2, plane2);
var relation = new Array (pfcCreate("pfcComponentConstraintType").ASM_CONSTRAINT_ALIGN, pfcCreate("pfcComponentConstraintType").ASM_CONSTRAINT_MATE);
var relationItem = new Array(pfcCreate("pfcModelItemType").ITEM_AXIS, pfcCreate("pfcModelItemType").ITEM_SURFACE);
var constrs = pfcCreate("pfcComponentConstraints");
    for (var i = 0; i < 2; i++)
    {
        var asmItem = subassembly.GetItemByName (relationItem[i], asmDatums [i]);
        if (asmItem == void null)
        {
            interactFlag = true;
            continue;
        }
        var compItem = componentModel.GetItemByName (relationItem[i], compDatums [i]);
        if (compItem == void null)
        {
            interactFlag = true;
            continue;
        }
        var MpfcSelect = pfcCreate ("MpfcSelect");
        var asmSel = MpfcSelect.CreateModelItemSelection (asmItem, subPath);
        var compSel = MpfcSelect.CreateModelItemSelection (compItem, void null);
        var constr = pfcCreate("pfcComponentConstraint").Create (relation[i]);
        constr.AssemblyReference  = asmSel;
        constr.ComponentReference = compSel;
        constr.Attributes = pfcCreate("pfcConstraintAttributes").Create (true, false);
        constrs.Append(constr);
    }
asmcomp.SetConstraints(constrs, void null);
}
// 以上為 axis_plane_assembly() 函式
///////////////////////////////////////////////////////////////////////////////////////////////////////////
// three_plane_assembly 採 align 組立, 若 featID 為 0 表示為空組立檔案
///////////////////////////////////////////////////////////////////////////////////////////////////////////
function three_plane_assembly(session, assembly, transf, featID, inc, part2, plane1, plane2, plane3, plane4, plane5, plane6){
var descr = pfcCreate("pfcModelDescriptor").CreateFromFileName ("v:/home/lego/nremsub6/"+part2);
var componentModel = session.GetModelFromDescr(descr);
var componentModel = session.RetrieveModel(descr);
if (componentModel != void null)
{
    var asmcomp = assembly.AssembleComponent (componentModel, transf);
}
var ids = pfcCreate("intseq");
// 若 featID 為 0 表示為空組立檔案
if (featID != 0){
    ids.Append(featID+inc);
    var subPath = pfcCreate("MpfcAssembly").CreateComponentPath(assembly, ids);
    subassembly = subPath.Leaf;
    }else{
    var subPath = pfcCreate("MpfcAssembly").CreateComponentPath(assembly, ids);
    subassembly = assembly;
    // 設法取得第一個組立零件 first_featID
    // 取得 assembly 項下的元件 id, 因為只有一個零件, 採用 index 0 取出其 featID
    var components = assembly.ListFeaturesByType(true, pfcCreate ("pfcFeatureType").FEATTYPE_COMPONENT);
    // 此一 featID 為組立件中的第一個零件編號, 也就是樂高人偶的 body
    var first_featID = components.Item(0).Id;
    }
var constrs = pfcCreate("pfcComponentConstraints");
var asmDatums = new Array(plane1, plane2, plane3);
var compDatums = new Array(plane4, plane5, plane6);
var MpfcSelect = pfcCreate("MpfcSelect");
for (var i = 0; i < 3; i++)
{
    var asmItem = subassembly.GetItemByName(pfcCreate("pfcModelItemType").ITEM_SURFACE, asmDatums[i]);
    
    if (asmItem == void null)
    {
        interactFlag = true;
        continue;
    }
    var compItem = componentModel.GetItemByName(pfcCreate("pfcModelItemType").ITEM_SURFACE, compDatums[i]);
    if (compItem == void null)
    {
        interactFlag = true;
        continue;
    }
    var asmSel = MpfcSelect.CreateModelItemSelection(asmItem, subPath);
    var compSel = MpfcSelect.CreateModelItemSelection(compItem, void null);
    var constr = pfcCreate("pfcComponentConstraint").Create(pfcCreate("pfcComponentConstraintType").ASM_CONSTRAINT_ALIGN);
    constr.AssemblyReference = asmSel;
    constr.ComponentReference = compSel;
    constr.Attributes = pfcCreate("pfcConstraintAttributes").Create (false, false);
    constrs.Append(constr);
}
asmcomp.SetConstraints(constrs, void null);
// 若 featID = 0 則傳回 first_featID
if (featID == 0)
    return first_featID;
}
// 以上為 three_plane_assembly() 函式
///////////////////////////////////////////////////////////////////////////////////////////////////////////
// three_plane_assembly2 採 mate 組立, 若 featID 為 0 表示為空組立檔案
///////////////////////////////////////////////////////////////////////////////////////////////////////////
function three_plane_assembly2(session, assembly, transf, featID, inc, part2, plane1, plane2, plane3, plane4, plane5, plane6){
var descr = pfcCreate("pfcModelDescriptor").CreateFromFileName ("v:/home/lego/nremsub6/"+part2);
var componentModel = session.GetModelFromDescr(descr);
var componentModel = session.RetrieveModel(descr);
if (componentModel != void null)
{
    var asmcomp = assembly.AssembleComponent (componentModel, transf);
}
var ids = pfcCreate("intseq");
// 若 featID 為 0 表示為空組立檔案
if (featID != 0){
    ids.Append(featID+inc);
    var subPath = pfcCreate("MpfcAssembly").CreateComponentPath(assembly, ids);
    subassembly = subPath.Leaf;
    }else{
    var subPath = pfcCreate("MpfcAssembly").CreateComponentPath(assembly, ids);
    subassembly = assembly;
    // 設法取得第一個組立零件 first_featID
    // 取得 assembly 項下的元件 id, 因為只有一個零件, 採用 index 0 取出其 featID
    var components = assembly.ListFeaturesByType(true, pfcCreate ("pfcFeatureType").FEATTYPE_COMPONENT);
    // 此一 featID 為組立件中的第一個零件編號, 也就是樂高人偶的 body
    var first_featID = components.Item(0).Id;
    }
var constrs = pfcCreate("pfcComponentConstraints");
var asmDatums = new Array(plane1, plane2, plane3);
var compDatums = new Array(plane4, plane5, plane6);
var MpfcSelect = pfcCreate("MpfcSelect");
for (var i = 0; i < 3; i++)
{
    var asmItem = subassembly.GetItemByName(pfcCreate("pfcModelItemType").ITEM_SURFACE, asmDatums[i]);
    
    if (asmItem == void null)
    {
        interactFlag = true;
        continue;
    }
    var compItem = componentModel.GetItemByName(pfcCreate("pfcModelItemType").ITEM_SURFACE, compDatums[i]);
    if (compItem == void null)
    {
        interactFlag = true;
        continue;
    }
    var asmSel = MpfcSelect.CreateModelItemSelection(asmItem, subPath);
    var compSel = MpfcSelect.CreateModelItemSelection(compItem, void null);
    var constr = pfcCreate("pfcComponentConstraint").Create(pfcCreate("pfcComponentConstraintType").ASM_CONSTRAINT_MATE);
    constr.AssemblyReference = asmSel;
    constr.ComponentReference = compSel;
    constr.Attributes = pfcCreate("pfcConstraintAttributes").Create (false, false);
    constrs.Append(constr);
}
asmcomp.SetConstraints(constrs, void null);
// 若 featID = 0 則傳回 first_featID
if (featID == 0)
    return first_featID;
}
// 以上為 three_plane_assembly2() 函式, 主要採三面 MATE 組立
//
// 假如 Creo 所在的操作系統不是 Windows 環境
if (!pfcIsWindows())
// 則啟動對應的 UniversalXPConnect 執行權限 (等同 Windows 下的 ActiveX)
netscape.security.PrivilegeManager.enablePrivilege("UniversalXPConnect");
// pfcGetProESession() 是位於 pfcUtils.js 中的函式, 確定此 JavaScript 是在嵌入式瀏覽器中執行
var session = pfcGetProESession();
// 設定 config option, 不要使用元件組立流程中內建的假設約束條件
session.SetConfigOption("comp_placement_assumptions","no");
// 建立擺放零件的位置矩陣, Pro/Web.Link 中的變數無法直接建立, 必須透過 pfcCreate() 建立
var identityMatrix = pfcCreate("pfcMatrix3D");
// 建立 identity 位置矩陣
for (var x = 0; x < 4; x++)
for (var y = 0; y < 4; y++)
{
    if (x == y)
        identityMatrix.Set(x, y, 1.0);
    else
        identityMatrix.Set(x, y, 0.0);
}
// 利用 identityMatrix 建立 transf 座標轉換矩陣
var transf = pfcCreate("pfcTransform3D").Create(identityMatrix);
// 取得目前的工作目錄
var currentDir = session.getCurrentDirectory();
// 以目前已開檔的空白組立檔案, 作為 model
var model = session.CurrentModel;
// 查驗有無 model, 或 model 類別是否為組立件, 若不符合條件則丟出錯誤訊息
if (model == void null || model.Type != pfcCreate("pfcModelType").MDL_ASSEMBLY)
throw new Error (0, "Current model is not an assembly.");
// 將此模型設為組立物件
var assembly = model;

/////////////////////////////////////////////////////////////////
// 開始執行組立, 全部採函式呼叫組立
/////////////////////////////////////////////////////////////////

// Body 與空組立檔案採三個平面約束組立
// 空組立面為 ASM_TOP, ASM_FRONT, ASM_RIGHT
// Body 組立面為 TOP, FRONT, RIGHT
//若 featID=0 表示為空組立檔案, 而且函式會傳回第一個組立件的 featID
//N_AXLE_5組立增量次序為 0
var featID = three_plane_assembly(session, assembly, transf, 0, 0, "N_B_ANGLE.prt", "ASM_TOP", "ASM_FRONT", "ASM_RIGHT", "TOP", "FRONT", "RIGHT"); 
//N_AXLE_10組立增量次序為 1
three_plane_assembly2(session, assembly, transf, featID, 0, 
                              "N_AXLE_10.prt",  "DTM2","RIGHT", "FRONT", "DTM1", "DTM2","FRONT");
//N_AXLE_5組立增量次序為 2
axis_plane_assembly(session, assembly, transf, featID, 0, 
                              "N_AXLE_5.prt", "A_25", "DTM2", "A_1", "DTM1");
//N_AXLE_5組立增量次序為 3
axis_plane_assembly(session, assembly, transf, featID, 0, 
                              "N_CROSS_2.prt", "A_26", "DTM1", "A_16", "DTM6");
//N_AXLE_5組立增量次序為 4
axis_plane_assembly(session, assembly, transf, featID, 0, 
                              "N_CROSS_2.prt", "A_26", "DTM6", "A_16", "DTM4");
//N_AXLE_5組立增量次序為 5
axis_plane_assembly(session, assembly, transf, featID, 4, 
                              "N_BUSHING.prt", "A_16", "DTM4", "A_15", "DTM1");
//N_AXLE_5組立增量次序為 6
axis_plane_assembly(session, assembly, transf, featID, 3, 
                              "N_BUSHING.prt", "A_16", "DTM4", "A_15", "DTM1");
//N_AXLE_5組立增量次序為 7
axis_plane_assembly(session, assembly, transf, featID, 3, 
                             "N_CONN_3.prt", "A_18", "DTM7", "A_20", "DTM1");
//N_AXLE_5組立增量次序為 8
axis_plane_assembly(session, assembly, transf, featID, 4, 
                             "N_CONN_3.prt", "A_18", "DTM8", "A_20", "DTM1");
//N_AXLE_5組立增量次序為 9
axis_plane_assembly(session, assembly, transf, featID, 0, 
                              "N_CROSS_2.prt", "A_25", "DTM6", "A_17", "DTM6");
//N_AXLE_5組立增量次序為 10
axis_plane_assembly(session, assembly, transf, featID, 0, 
                              "N_CROSS_2.prt", "A_25", "DTM1", "A_17", "DTM4");
//N_AXLE_5組立增量次序為 11
axis_plane_assembly(session, assembly, transf, featID, 9, 
                              "N_CROSS_2.prt", "A_17", "DTM6", "A_17", "DTM4");
//N_AXLE_5組立增量次序為 12
axis_plane_assembly(session, assembly, transf, featID, 10, 
                              "N_CROSS_2.prt", "A_17", "DTM6", "A_17", "DTM4");
//N_AXLE_5組立增量次序為 13
axis_plane_assembly(session, assembly, transf, featID, 8, 
                              "N_BEAM_3.prt", "A_20", "DTM1", "A_38", "TOP");
//N_AXLE_5組立增量次序為 14
axis_plane_assembly(session, assembly, transf, featID, 7, 
                              "N_BEAM_3.prt", "A_20", "DTM1", "A_38", "TOP");

// regenerate 並且 repaint 組立檔案
assembly.Regenerate (void null);
session.GetModelWindow (assembly).Repaint();    
</script>
</body>
</html>
'''
        return outstring