clc
clear all
load("data.mat")

x_axis = [];
y_axis = [];
z_axis = [];
mark = [];
for x = 1:64
    for y = 1:64
        for z = 1:64
            c = data(x,y,z);
            if c == 0
                continue
            elseif c == 1
%                 coord = [...
%     x - 1    y - 1     z - 1;
%     x   y - 1    z - 1;
%     x   y   z - 1;
%     x - 1   y   z - 1;
%     x - 1   y - 1    z ;
%     x   y - 1   z ;
%     x   y   z ;
%     x - 1   y   z ;];
%     idx = [4 8 5 1 4; 1 5 6 2 1; 2 6 7 3 2; 3 7 8 4 3; 5 8 7 6 5; 1 4 3 2 1]';
%                 patch('vertices', coord, 'faces', idx', 'facecolor', 'r', 'facealpha', 1);
                color = 'r';
            elseif c == 2
;
                color = 'b';
            elseif c == 3
                color = 'y';
            elseif c == 4
                color = 'g';
            elseif c == 5
                color = 'r';
            elseif c == 6
                color = 'c';
            else 
                color = 'm';
            end
            x_axis(end+1) = x;
            y_axis(end+1) = y;
            z_axis(end+1) = z;
            mark(end+1) = c;
        end
    end
end
h = scatter3(x_axis, y_axis, z_axis, 10, mark, 's');
view(3);
xlabel('X')
ylabel('Y')
zlabel('Z')
h.MarkerFaceColor = 'flat';
%h.MarkerFaceAlpha = .2;
grid on
colormap(jet)
colorbar