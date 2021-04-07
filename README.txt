第一种：单接口测试 每个每个接口都是独立的 优先覆盖
第二种：业务流的测试  多个接口串联调用  业务流成功的前提是单接口没有问题


一个表单一个接口
一个表单所有的接口
一个测试类一个接口

充值接口遇到的第一个问题：类型问题
    用户充值之前的余额：{'leave_amount': Decimal('2000887.00')}
    处理sql语句：把Decimal对应的字段修改为字符串返回 CAST(字段名 AS CHAR)
    SELECT CAST(leave_amount AS CHAR)as amount FROM member WHERE id=#member_id#
方式2：
