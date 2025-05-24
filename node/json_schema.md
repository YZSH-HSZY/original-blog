# JSON SCHEMA

JSON Schema 旨在定义 JSON 数据的验证、文档、超链接导航和交互控制

> 参考文档:
> - [json-schema官方文档](https://json-schema.org/)
> - [json-schema草案文档](https://www.learnjsonschema.com/2020-12/)

## USAGE

### KEY

#### core

- `$schema`: 声明模式具有指定草案dialect规范
> 目前存在的草案有`Draft 4`(http://json-schema.org/draft-04/schema#)/`Draft 6`(http://json-schema.org/draft-06/schema#)/`Draft 7`(http://json-schema.org/draft-07/schema#)/`Draft 2019-09`(http://json-schema.org/draft-07/schema#)
> Example: `"$schema": "http://json-schema.org/draft-04/schema#"`

#### Applicator
- `oneOf`: 将一个或多个子模式应用于实例中的特定位置, 并组合或修改其结果
> 如果实例针对此关键字的值定义的一个架构成功验证，则该实例针对此关键字成功验证

