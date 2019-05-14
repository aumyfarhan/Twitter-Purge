filename_purged='purged_favourites_vs_user.csv';
purged=csvread(filename_purged);
x_purged=purged(:,1);
y_purged=purged(:,2);

filename_random='random_favourites_vs_user.csv';
random=csvread(filename_random);
x_random=random(:,1);
y_random=random(:,2);

figure,plot(x_purged,y_purged,'ro--'),hold on;
xlabel('Number of favourites','FontSize',18),...
    ylabel('CDF','FontSize',18);
set(gca,'XScale','log');
plot(x_random,y_random,'b*:')
%title ('User CDF vs No of Favourites')
legend ({'Purged','Random'},'FontSize',14);
    