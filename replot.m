load("history/agent1.csv")
load("history/agent2.csv")
load("history/agent3.csv")
load("history/agent4.csv")
load("history/agent5.csv")
load("history/agent6.csv")
load("history/agent7.csv")
load("history/agent8.csv")
load("history/agent9.csv")
load("history/agent10.csv")
load("history/agent11.csv")
load("history/agent12.csv")
load("history/agent13.csv")
load("history/agent14.csv")
load("history/agent15.csv")
load("history/agent16.csv")
load("history/agent17.csv")
load("history/agent18.csv")
load("history/agent19.csv")
load("history/agent20.csv")
load("history/agent21.csv")
load("history/agent22.csv")
load("history/agent23.csv")
load("history/agent24.csv")
load("history/agent25.csv")
load("history/agent26.csv")
load("history/agent27.csv")
load("history/agent28.csv")
load("history/agent29.csv")
load("history/agent30.csv")
load("history/agent31.csv")
load("history/agent32.csv")
load("history/agent33.csv")
load("history/agent34.csv")
load("history/agent35.csv")
load("history/agent36.csv")
load("history/agent37.csv")
load("history/agent38.csv")
load("history/agent39.csv")
load("history/agent40.csv")
a = zeros(10, 1);
a(1) = length(agent1)
a(2) = length(agent2)
a(3) = length(agent3)
a(4) = length(agent4)
a(5) = length(agent5)
a(6) = length(agent6)
a(7) = length(agent7)
a(8) = length(agent8)
a(9) = length(agent9)
a(10) = length(agent10)
mean(a)
%%
a(11) = length(agent11)
a(12) = length(agent12)
a(13) = length(agent13)
a(14) = length(agent14)
a(15) = length(agent15)
a(16) = length(agent16)
a(17) = length(agent17)
a(18) = length(agent18)
a(19) = length(agent19)
a(20) = length(agent20)
a(21) = length(agent21)
a(22) = length(agent22)
a(23) = length(agent23)
a(24) = length(agent24)
a(25) = length(agent25)
a(26) = length(agent26)
a(27) = length(agent27)
a(28) = length(agent28)
a(29) = length(agent29)
a(30) = length(agent30)
a(31) = length(agent31)
a(32) = length(agent32)
a(33) = length(agent33)
a(34) = length(agent34)
a(35) = length(agent35)
a(36) = length(agent36)
a(37) = length(agent37)
a(38) = length(agent38)
a(39) = length(agent39)
a(40) = length(agent40)
mean(a)

%%
%plot 
%0 is free space, 99 means permnant obstacle, 100 means temprary obstacle, 101 means regular flight
load("history/reservedMap0.csv")
cmap = colormap(jet);
for x = 1:512
    for y = 1:512
        c = reservedMap0(x,y);
        if c == 0
            rectangle('Position',[x y 1 1], 'FaceColor',[1 1 1] )
        elseif c == 99
            rectangle('Position',[x y 1 1], 'FaceColor',[0 0 0])
        elseif c == 100
            rectangle('Position',[x y 1 1], 'FaceColor','g')
        elseif c == 101
            rectangle('Position',[x y 1 1], 'FaceColor',[0 0 0] )
        else
            rectangle('Position',[x y 1 1], 'FaceColor',cmap(c * 3, :) )
        end
    end
end
axis square
axis([0 512 0 512])
cmap = colormap(jet)
colorbar