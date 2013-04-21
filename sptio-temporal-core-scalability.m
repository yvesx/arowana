clear all; close all;
y = [1 4 8 16]; 
x = [100 250 600 1400];

zlim([500 40000])
[X,Y] = meshgrid(x,y);
set(gca,'ZScale','log')
% arowana
Z = [554	2010	4880	17894;289	1389	3103	11094;187	809	1985	7093;149	578	1480	5680];  

aros = surf(X,Y,Z); hold on;
set(aros,'FaceColor',[1 0 0],'FaceAlpha',0.8);
% arowanaU
Z= [534	1889	4207	13908;266	1309	2781	7178;164	742	1608	4129;129	509	1109	2766]; 
arous = surf(X,Y,Z);
set(arous,'FaceColor',[0 1 0],'FaceAlpha',0.8);
% btree
Z = [5598	16081	34399	91306;5302	18163	35199	92113;5703	19081	71028	170421;6224	52428 264312 353901];
bs = surf(X,Y,Z);
set(bs,'FaceColor',[0 0 1],'FaceAlpha',0.8);

% btree par
Z=[3769	8292	20102	38809;2618	3984	9504	20560;2478	3609	9398	21008;2590	3979	9781	24582];
zlim('manual')
zlim([500 40000])
bps = surf(X,Y,Z,'FaceColor','interp','FaceLighting','phong');
set(bps,'FaceColor',[0 1 1],'FaceAlpha',0.8);
xlabel('# of Connections in data (in millions)','FontSize',14)
ylabel('# of threads used','FontSize',14)
zlabel('Time to index (in seconds)','FontSize',16)
%camlight right;
AX=legend('Arwn','ArwnU','BTree','BTreePar');
LEG = findobj(AX,'type','text');
set(LEG,'FontSize',16)
% 
% subplot(1,3,2);
% Z = 2*Y;  surf(X,Y,Z);
% title('z=2y');
% 
% subplot(1,3,3);
% Z = zeros(length(y),length(x));
% Z(1:end,1:end)=2;
% surf(X,Y,Z);
% title('z=2');
% 
% A=[-2 -1 1;0 -2 1;0 0 1]; 
% b=[0;0;2];
% sol=A\b;
% 
% figure;
% surf(X,Y,2*X + Y); hold on;
% surf(X,Y,2*Y); 
% surf(X,Y,Z);

%now add the point of intersection from the solution
%plot3(sol(1),sol(2),sol(3),'k.','MarkerSize',30)
title('Indexing time for different indices, data sizes, threads used','FontSize',14);