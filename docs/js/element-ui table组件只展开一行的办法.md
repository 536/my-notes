# element-ui table组件只展开一行的办法

```js
<el-table ref="demoTable" @row-dblclick="row_expand" @expand-change="expandChange"></el-table>
Vue({
    methods: {
        row_expand(row, column, event) {
            this.$refs.linkTable.toggleRowExpansion(row);
        },
        expandChange(row, expandedRows){
            if (expandedRows.indexOf(row) != -1) {
                // 当前行展开时
                expandedRows.forEach(i=>{
                    if (row != i) {
                        // 折叠所有其他展开的行
                        this.$refs.demoTable.toggleRowExpansion(i);
                    }
                })
            }
        },
    },
})
```

思路就是在`expandChange`事件触发时，根据`expandedRows`中的展开行列表，判断是否为当前行，不是当前行的就折叠
