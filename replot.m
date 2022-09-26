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
a = zeros(10, 1);
a(1) = length(agent1);
a(2) = length(agent2);
a(3) = length(agent3);
a(4) = length(agent4);
a(5) = length(agent5);
a(6) = length(agent6);
a(7) = length(agent7);
a(8) = length(agent8);
a(9) = length(agent9);
a(10) = length(agent10);
mean(a);
%%
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
%%
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
%%
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
%%
load("history/agent41.csv")
load("history/agent42.csv")
load("history/agent43.csv")
load("history/agent44.csv")
load("history/agent45.csv")
load("history/agent46.csv")
load("history/agent47.csv")
load("history/agent48.csv")
load("history/agent49.csv")
load("history/agent50.csv")
a(41) = length(agent41)
a(42) = length(agent42)
a(43) = length(agent43)
a(44) = length(agent44)
a(45) = length(agent45)
a(46) = length(agent46)
a(47) = length(agent47)
a(48) = length(agent48)
a(49) = length(agent49)
a(50) = length(agent50)

%%


%%
%plot 
%0 is free space, 99 means permnant obstacle, 100 means temprary obstacle, 101 means regular flight
for i = 3:3
fig = figure(i);
%F = sprintf('history/reservedMap%d.csv', i);
F = sprintf("history/reservedMapTest.csv");
reservedMap = load(F);
cmap = colormap(lines);
for x = 1:512
    for y = 1:512
        c = reservedMap(x,y);
        if c == 0
            
        elseif c == 99
            rectangle('Position',[x y 1 1], 'FaceColor',[0 0 0],'EdgeColor', [0, 0, 0], 'LineWidth', 0.001)
        elseif c == 100
            rectangle('Position',[x y 1 1], 'FaceColor','b','EdgeColor', 'b')
        elseif c == 101
            rectangle('Position',[x y 1 1], 'FaceColor','r', 'EdgeColor', 'g','LineWidth', 0.001 )
        else
            rectangle('Position',[x y 1 1], 'FaceColor',cmap(c * 3, :), 'EdgeColor', cmap(c * 3, :),'LineWidth', 0.001 )
        end
    end
end
rectangle('Position',[agent1(min(length(agent1), i),1) agent1(min(length(agent1), i),2) 5 5], 'FaceColor', cmap(1 * 3, :),'EdgeColor', cmap(1 * 3, :), 'LineWidth', 0.001)
rectangle('Position',[agent2(min(length(agent2), i),1) agent2(min(length(agent2), i),2) 5 5], 'FaceColor', cmap(2 * 3, :),'EdgeColor', cmap(2 * 3, :), 'LineWidth', 0.001)
rectangle('Position',[agent3(min(length(agent3), i),1) agent3(min(length(agent3), i),2) 5 5], 'FaceColor', cmap(3 * 3, :),'EdgeColor', cmap(3 * 3, :), 'LineWidth', 0.001)
rectangle('Position',[agent4(min(length(agent4), i),1) agent4(min(length(agent4), i),2) 5 5], 'FaceColor', cmap(4 * 3, :),'EdgeColor', cmap(4 * 3, :), 'LineWidth', 0.001)
rectangle('Position',[agent5(min(length(agent5), i),1) agent5(min(length(agent5), i),2) 5 5], 'FaceColor', cmap(5 * 3, :),'EdgeColor', cmap(5 * 3, :), 'LineWidth', 0.001)
rectangle('Position',[agent6(min(length(agent6), i),1) agent6(min(length(agent6), i),2) 5 5], 'FaceColor', cmap(6 * 3, :),'EdgeColor', cmap(6 * 3, :), 'LineWidth', 0.001)
rectangle('Position',[agent7(min(length(agent7), i),1) agent7(min(length(agent7), i),2) 5 5], 'FaceColor', cmap(7 * 3, :),'EdgeColor', cmap(7 * 3, :), 'LineWidth', 0.001)
rectangle('Position',[agent8(min(length(agent8), i),1) agent8(min(length(agent8), i),2) 5 5], 'FaceColor', cmap(8 * 3, :),'EdgeColor', cmap(8 * 3, :), 'LineWidth', 0.001)
rectangle('Position',[agent9(min(length(agent9), i),1) agent9(min(length(agent9), i),2) 5 5], 'FaceColor', cmap(9 * 3, :),'EdgeColor', cmap(9 * 3, :), 'LineWidth', 0.001)
rectangle('Position',[agent10(min(length(agent10), i),1) agent10(min(length(agent10), i),2) 5 5], 'FaceColor', cmap(10 * 3, :),'EdgeColor', cmap(10 * 3, :), 'LineWidth', 0.001)
axis square
axis([0 512 0 512])
%str = sprintf("ten agents moving time:%d", i);
str = sprintf("Realistic Map");
title(str)
%filename = sprintf("special map test ten agents moving time%d.png", i);
filename = 'Realistic Map.png';
print(filename, '-dpng', '-r600');
close(fig)
end
%%
%plot for papaer
for i = 1:1
load("figure/agent1.csv")
load("figure/agent2.csv")
load("figure/agent3.csv")
load("figure/agent4.csv")
load("figure/agent5.csv")
load("figure/agent6.csv")
load("figure/agent7.csv")
load("figure/agent8.csv")
load("figure/agent9.csv")
load("figure/agent10.csv")
fig = figure(i);
%F = sprintf('history/reservedMap%d.csv', i);
F = sprintf("figure/MSAstarStressed.csv");
reservedMap = load(F);
cmap = colormap(lines);
for x = 1:512
    for y = 1:512
        c = reservedMap(x,y);
        if c == 0
            
        elseif c == 99
            rectangle('Position',[x y 1 1], 'FaceColor',[0 0 0],'EdgeColor', [0, 0, 0], 'LineWidth', 0.001)
        elseif c == 100
            rectangle('Position',[x y 1 1], 'FaceColor','b','EdgeColor', 'b')
        elseif c == 101
            rectangle('Position',[x y 1 1], 'FaceColor','g', 'EdgeColor', 'g','LineWidth', 0.001 )
        else
            rectangle('Position',[x y 1 1], 'FaceColor',cmap(c * 3, :), 'EdgeColor', cmap(c * 3, :),'LineWidth', 0.001 )
        end
    end
end
rectangle('Position',[agent1(min(length(agent1), i),1) agent1(min(length(agent1), i),2) 2 2], 'FaceColor', cmap(1 * 3, :),'EdgeColor', cmap(1 * 3, :), 'LineWidth', 0.001)
rectangle('Position',[agent2(min(length(agent2), i),1) agent2(min(length(agent2), i),2) 2 2], 'FaceColor', cmap(2 * 3, :),'EdgeColor', cmap(2 * 3, :), 'LineWidth', 0.001)
rectangle('Position',[agent3(min(length(agent3), i),1) agent3(min(length(agent3), i),2) 2 2], 'FaceColor', cmap(3 * 3, :),'EdgeColor', cmap(3 * 3, :), 'LineWidth', 0.001)
rectangle('Position',[agent4(min(length(agent4), i),1) agent4(min(length(agent4), i),2) 2 2], 'FaceColor', cmap(4 * 3, :),'EdgeColor', cmap(4 * 3, :), 'LineWidth', 0.001)
rectangle('Position',[agent5(min(length(agent5), i),1) agent5(min(length(agent5), i),2) 2 2], 'FaceColor', cmap(5 * 3, :),'EdgeColor', cmap(5 * 3, :), 'LineWidth', 0.001)
rectangle('Position',[agent6(min(length(agent6), i),1) agent6(min(length(agent6), i),2) 2 2], 'FaceColor', cmap(6 * 3, :),'EdgeColor', cmap(6 * 3, :), 'LineWidth', 0.001)
rectangle('Position',[agent7(min(length(agent7), i),1) agent7(min(length(agent7), i),2) 2 2], 'FaceColor', cmap(7 * 3, :),'EdgeColor', cmap(7 * 3, :), 'LineWidth', 0.001)
rectangle('Position',[agent8(min(length(agent8), i),1) agent8(min(length(agent8), i),2) 2 2], 'FaceColor', cmap(8 * 3, :),'EdgeColor', cmap(8 * 3, :), 'LineWidth', 0.001)
rectangle('Position',[agent9(min(length(agent9), i),1) agent9(min(length(agent9), i),2) 2 2], 'FaceColor', cmap(9 * 3, :),'EdgeColor', cmap(9 * 3, :), 'LineWidth', 0.001)
rectangle('Position',[agent10(min(length(agent10), i),1) agent10(min(length(agent10), i),2) 2 2], 'FaceColor', cmap(10 * 3, :),'EdgeColor', cmap(10 * 3, :), 'LineWidth', 0.001)
axis square
axis([0 512 0 512])
%str = sprintf("ten agents moving time:%d", i);
%str = sprintf("Ten Agents Searching in Simulated Map with A*");
str = sprintf("Ten Agents Searching in Stressed Map with MSA*");
title(str)
%filename = sprintf("special map test ten agents moving time%d.png", i);
filename = 'figure/MAstarstressed.png';
print(filename, '-dpng', '-r600');
close(fig)
end