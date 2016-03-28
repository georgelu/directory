diff <(cat ../directory.json | sed 's/}, {/},\n{/g'|head -1) <(cat input.json | sed 's/},{/},\n{/g'| head -1 )
diff <(cat food-neighborhood.csv | head -2 ) \
     <(cat input.json | sed 's/},{/},\n{/g'|  head -1 | sed 's/","/",\n"/g' )
