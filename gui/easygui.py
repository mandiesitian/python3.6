import easygui as g;
import sys;

while(1):
    g.msgbox('嗨，欢迎进入第一个界面小游戏');

    msg='请问你希望在这里学到什么';
    title='小游戏互动';

    choises=['谈恋爱','编程','OOXX','琴棋书画'];
    choise=g.choicebox(msg,title,choise);
    g.msgbox('你的选择是'+str(choise),'结果');
    msg='你希望重新开始此游戏吗';
    title='请选择';

    if g.ccbox(msg,title):
        pass;
    else:
        sys.exit(0);
