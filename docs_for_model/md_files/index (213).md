# Настройка архива вложенных документов

## Общее описание

Настройка архива вложенных документов необходима для работы аналитической формы [Архив вложенных документов](https://ecm-user-manuals.readthedocs.io/ru/latest/User%20manuals/Работа%20со%20вложениями/#архив_документов) и происходит в несколько этапов:

* В документ «Справочники поисковой системы» заносятся поля для фильтра, по которым будут собираться вложения.
* В справочник «Итоговые выборки поисковой системы» добавить документ с выборкой из некоторой таблицы для документа или группы документов, если их сущности извлекаются одинаково.
* В документе "Настройка документа" на вкладке "Контекстный поиск" заполнить несколько полей.
* Обновить страницу (клавиша F5), чтобы изменения вступили в силу.

## Справочники поисковой системы

Чтобы открыть документ «Справочники поисковой системы», необходимо в Меню в поисковой строке ввести - «Справочники поисковой системы».

Откроется документ "Справочники FTS". В нём необходимо заполнить таблицу "Фильтры".

![Справочники FTS](./media/CustomFTSFiltersForm.png)

| Id                 | Name                | Description |
| ------------------ | ------------------- | ----------- |
| Contractor         | Контрагент          |
| Contract           | Договор             |
| SignatoryUser      | Работник            |
| Project            | Проект              |
| Initiator          | Инициатор           |
| CUser              | Создатель документа |
| Curator            | Куратор             |
| StageUser          | Участник маршрута   |
| EmpowermentSubject | Полномочия          |
| Filial             | Организация         |
| Subtype            | Подтип              |

Существует строго определённый набор значений поля "Id", приведённый в [таблице ниже](#таблица). Соответствующее им поле "Name" заполняется произвольно. В справочнике «Итоговые выборки поисковой системы» этим значениям будут поставлены в соответствие поля в таблицах, по которым будет осуществляться поиск и фильтрация документов с вложениями.

<!-- ### Примеры поисковых запросов

<table>
  <thead>
    <tr>
      <th>Имя</th>
      <th>Запрос</th>
      <th>Поля</th>
    </tr>
  </thead>
    <tbody>
      <tr>
        <td>Route</td>
        <td>
            ```sql
            SELECT t."DocCode", t."DocType" FROM comdoc."Route" AS t
            ```
        </td>
  <td>DocName, DocSubject</td>
  </tr>
  <tr>
    <tr>
      <td>Акты аннулирования</td>
      <td>
      ```sql
      SELECT t."VCode" AS "DocCode", t."TypeName" AS "DocType" FROM dfd."CancellationAct" AS t
      ```
      </td>
      <td>Subject, DocTypeName, DocCode</td>
    </tr>
    <tr>
      <td>Графики отпусков</td>
      <td>
      ```sql
      SELECT t."VCode" AS "DocCode", t."TypeName" AS "DocType" FROM aw."RP_DocVacation" AS t
      ```
      </td>
      <td>NumDoc, NameDoc, Year, Note</td>
    </tr>
    <tr>
      <td>Дин. атрибуты: договоры</td>
      <td>
      ```sql
      select t."DocCode", t."DocType" from ( SELECT d."VCode" AS "DocCode", 
      d."TypeName" AS "DocType", t.* FROM comdoc."DocflowExists" AS d 
      join dfd."DocumentConstructor" dc on d."DocumentCategory" = dc."VCode" 
      join dfd."DocumentCategoryAttributeType" dcat on dc."VCode" = dcat."PCode" 
      join dfd."DocumentAdditionalAttribute" AS a 
      ON dcat."VCode" = a."CategoryAttributeType" 
      and d."VCode" = a."PCode" and dcat."AttributeType" = 'Base.Contract' 
      join contract."VContract" t on a."BigIntValue" = t."VCode" ) as t
      ```
      </td>
      <td>Name</td>
    </tr>
    <tr>
      <td>Дин. атрибуты: должность</td>
      <td>
      ```sql
      select t."DocCode", t."DocType" 
      from ( SELECT d."VCode" AS "DocCode", d."TypeName" AS "DocType", t.* FROM comdoc."DocflowExists" AS d 
      join dfd."DocumentConstructor" dc on d."DocumentCategory" = dc."VCode" 
      join dfd."DocumentCategoryAttributeType" dcat on dc."VCode" = dcat."PCode" 
      join dfd."DocumentAdditionalAttribute" AS a ON dcat."VCode" = a."CategoryAttributeType" 
      and d."VCode" = a."PCode" and dcat."AttributeType" = 'Base.Post' 
      join rp."RP_Post" t on a."BigIntValue" = t."VCode" ) as t
      ```
</td>
      <td>Name</td>
    </tr>
    <tr>
      <td>Дин. атрибуты: контрагенты</td>
      <td>
```sql
select t."DocCode", t."DocType" from ( SELECT d."VCode" AS "DocCode", d."TypeName" AS "DocType", t.* 
FROM comdoc."DocflowExists" AS d join dfd."DocumentConstructor" dc 
on d."DocumentCategory" = dc."VCode" join dfd."DocumentCategoryAttributeType" dcat 
on dc."VCode" = dcat."PCode" join dfd."DocumentAdditionalAttribute" AS a 
ON dcat."VCode" = a."CategoryAttributeType" and d."VCode" = a."PCode" 
and dcat."AttributeType" = 'Base.Contractor' join comdoc."Contractor" t 
on a."BigIntValue" = t."VCode" ) as t
```
</td>
      <td>FullName, Name</td>
    </tr>
    <tr>
      <td>Дин. атрибуты: подразделение</td>
      <td>
```sql
select t."DocCode", t."DocType" 
from ( SELECT d."VCode" AS "DocCode", d."TypeName" AS "DocType", t.* 
FROM comdoc."DocflowExists" AS d join dfd."DocumentConstructor" dc 
on d."DocumentCategory" = dc."VCode" join dfd."DocumentCategoryAttributeType" dcat 
on dc."VCode" = dcat."PCode" join dfd."DocumentAdditionalAttribute" AS a 
ON dcat."VCode" = a."CategoryAttributeType" and d."VCode" = a."PCode" 
and dcat."AttributeType" = 'Base.Department' join comdoc."Department" t 
on a."BigIntValue" = t."VCode" ) as t
```
</td>
      <td>FullName, Name</td>
    </tr>
    <tr>
      <td>Дин. атрибуты: польз. тип атрибутов</td>
      <td>
```sql
select t."DocCode", t."DocType" 
from ( SELECT d."VCode" AS "DocCode", d."TypeName" AS "DocType", t.* 
FROM comdoc."DocflowExists" AS d join dfd."DocumentConstructor" dc 
on d."DocumentCategory" = dc."VCode" 
join dfd."DocumentCategoryAttributeType" dcat on dc."VCode" = dcat."PCode" 
join dfd."DocumentAdditionalAttribute" AS a ON dcat."VCode" = a."CategoryAttributeType" 
and d."VCode" = a."PCode" and dcat."AttributeType" = 'Base.Unispr' 
join dfd."Unispr" t on a."BigIntValue" = t."VCode" ) as t
```
</td>
      <td>Name, AddInfo</td>
    </tr>
    <tr>
      <td>Дин. атрибуты: простые</td>
      <td>
```sql
select t."DocCode", t."DocType" from 
( SELECT d."VCode" AS "DocCode", d."TypeName" AS "DocType", t.*,
 comdoc."DTOC"(t."DateValue") as "DateFormatted" FROM comdoc."DocflowExists" 
 AS d join dfd."DocumentConstructor" dc on d."DocumentCategory" = dc."VCode" 
 join dfd."DocumentCategoryAttributeType" dcat on dc."VCode" = dcat."PCode" 
 join dfd."DocumentAdditionalAttribute" AS t ON dcat."VCode" = t."CategoryAttributeType" 
 and d."VCode" = t."PCode" and dcat."AttributeType" 
 in ('Date', 'bigint', 'double', 'money', 'string', 'longstring', 'DateTime', 'Time') ) as t
```
</td>
      <td>DateFormatted, DateValue, Value, BigIntValue, DoubleValue, MoneyValue, DateTimeValue, TimeValue</td>
    </tr>
    <tr>
      <td>Дин. атрибуты: работник</td>
      <td>
```sql
select t."DocCode", t."DocType" from 
( SELECT d."VCode" AS "DocCode", d."TypeName" AS "DocType", t.* 
FROM comdoc."DocflowExists" AS d join dfd."DocumentConstructor" dc 
on d."DocumentCategory" = dc."VCode" 
join dfd."DocumentCategoryAttributeType" dcat on dc."VCode" = dcat."PCode" 
join dfd."DocumentAdditionalAttribute" AS a ON dcat."VCode" = a."CategoryAttributeType" 
and d."VCode" = a."PCode" and dcat."AttributeType" = 'Base.RP_Worker' 
join rp."RP_Worker" t on a."BigIntValue" = t."VCode" ) as t
```
</td>
      <td>NameFull, NameShort</td>
    </tr>
    <tr>
      <td>Договора</td>
      <td>
```sql
SELECT t."VCode" AS "DocCode", t."TypeName" AS "DocType" FROM contract."Contract" AS t
```
</td>
      <td>SubjectOfContract, Number, ContentContract, GoalContract, SpecialCondition, VnNumber</td>
    </tr>
    <tr>
      <td>Заявки на выпуск</td>
      <td>
```sql
SELECT t."VCode" AS "DocCode", t."TypeName" AS "DocType" FROM comdoc."ECPCertificateApplication" AS t
```
</td>
      <td>DocumentNumber, FullName, DocflowUser</td>
    </tr>
    <tr>
      <td>Заявки на отзыв</td>
      <td>
```sql
SELECT t."VCode" AS "DocCode", t."TypeName" AS "DocType" FROM comdoc."ECPCertificateRevocation" AS t
```
</td>
      <td>DocumentNumber, DocumentDate, FullName, Note</td>
    </tr>
    <tr>
      <td>Заявки на планирование отпусков</td>
      <td>
```sql
SELECT t."VCode" AS "DocCode", t."TypeName" AS "DocType" FROM vac."VacationRequest" AS t
```
</td>
      <td>DocumentNumber, Note, PlanYear</td>
    </tr>
    <tr>
      <td>КЭДО</td>
      <td>
```sql
SELECT t."VCode" AS "DocCode", t."TypeName" AS "DocType" FROM dfd."UniversalDocument" AS t
```
</td>
      <td>Text, DocumentNumber, DocumentDate</td>
    </tr>
    <tr>
      <td>Канцелярия</td>
      <td>
```sql
SELECT t."VCode" AS "DocCode", t."TypeName" AS "DocType" FROM dfd."DocflowDocument" AS t
```
</td>
      <td>Text, Subject, DocumentNumber</td>
    </tr>
    <tr>
      <td>Приложения</td>
      <td>
```sql
SELECT t."VCode" AS "DocCode", t."TypeName" AS "DocType" FROM contract."AdditionalContract" AS t
```
</td>
      <td>SubjectOfContract, Number</td>
    </tr>
    <tr>
      <td>Трудовые договоры</td>
      <td>
```sql
SELECT t."VCode" AS "DocCode", t."TypeName" AS "DocType" FROM rp."RP_WorkContract" AS t
```
</td>
      <td>NumDoc, DateDoc</td>
    </tr>
  </tbody>
</table> -->

<!-- ## Итоговые выборки поисковой системы

Чтобы открыть справочник «Итоговые выборки поисковой системы», необходимо в меню в папке "Администрирование", подпапке "Документооборот", подпапке "Поисковая система" выбрать пункт «Итоговые выборки поисковой системы».

![Меню](./media/ResultFTSMenu.png)

Откроется реестр "Итоги FTS".

![Итоги FTS](./media/ResultFTSRegistry.png)

Значения этого справочника будут предлагаться для выбора в документе ["Настройка документа"](../Настройка документов/index.md). Для создания нового документа необходимо нажать на кнопку "Создать" на верхней панели инструментов.

![Кнопка "Создать"](./media/create.png)

В поле "Выборка" необходимо ввести обозначение для документа или группы документов, если их сущности извлекаются одинаково, которое будет использоваться в качестве одного из значений в настройках документов. В поле "Примечание" можно внести пояснения, например, к каким именно документам относится выборка.

![Пример заполнения полей "Выборка" и "Примечание"](./media/ResultFTSHeader.png)

Под полем "Выборка" необходимо прописать результирующий селект, который в процессе расчета будет выполнять система. Структура селекта для всех выборок должна быть одинаковой, они будут объединяться с помощью оператора ```UNION```. Выборка состоит из следующих полей:

* ```DocCode``` - уникальный код документа, используемый в системе; как правило ```VCode```.
* ```DocType``` - тип документа; как правило ```TypeName```.
* ```DocDate``` - дата документа; свойство, которое указывается в *Настройке документа* и передаётся в качестве параметра; указывается ```:DateProperty```.
* ```DocNumber``` - номер документа; свойство, которое указывается в *Настройке документа* и передаётся в качестве параметра; указывается ```:NumberProperty```.
* ```ContractorId``` - уникальный код контрагента, используемый в системе.
* ```ContractId``` - уникальный код договора, используемый в системе.
* ```AddContractId``` - уникальный код дополнительного документа к договору, используемый в системе.
* ```ProjectId``` - уникальный код проекта, используемый в системе.

В зависимости от подключаемых документов будут меняться таблица, стоящая после оператора ```FROM```, и присваиваемые значения установленных в селекте полей. Если для них есть соответствующие им поля в таблице, их необходимо присвоить. Например, полю ```ContractId``` должен соответствовать код договора, который есть в таблице ```dbo.DocflowDocument``` под названием ```Contract```. Если такого поля в таблице нет, необходимо присвоить значение ```null```. Например, в таблице ```dbo.DocflowDocument``` не указывается код дополнительного документа к договору, поэтому значению ```AddContractId``` присваивется ```null```.

**В левую часть указывается скрипт:**

```sql
SELECT t."VCode" AS "DocCode"
     , t."TypeName" AS "DocType"
     , :DateProperty AS "DocDate"
     , :NumberProperty AS "DocNumber"
     , NULL::bigint AS "ContractorId"
     , NULL::bigint AS "ContractId"
     , NULL::bigint AS "AddContractId"
     , NULL::bigint AS "ProjectId"
FROM dfd."UniversalDocument" as t
WHERE 1 = 1

```

**В правую часть:**

```sql
SELECT t."VCode" AS "DocCode"
     , t."TypeName" AS "DocType"
     , :DateProperty AS "DocDate"
     , :NumberProperty AS "DocNumber"
     , NULL AS "DocName"
     , NULL AS "DocTheme"
     , NULL AS "DocDefinition"
FROM dfd."UniversalDocument" as t
WHERE 1 = 1
```

В таблицу справа "Фильтры" необходимо занести значения из *Справочника поисковой системы*, по которым будет осуществляться фильтр, и SQL-скрипт – кусок кода, который будет подставлен в предложение WHERE результирующего селекта. Значение, сравниваемое с ```an.Value```, будет совпадать со значением в столбце ```ID``` таблицы "Фильтр". Значение, сравниваемое с ```an.Value```, будет совпадать с полем таблицы, которое присваивается одному из полей селекта. 

<!-- ![Пример документа "Итог FTS"](./media/ResultFTSForm.png) -->

<!-- В табличную часть "Фильтры" указывается следующее:

**CUser - Создатель документа**
```sql
and exists(
select 1 from "tmp_anFilters_for_documentSearch" as an where an."id" = 'CUser' and an."value" = cast(t."CUser" as character varying)
)
```

**Initiator - Инициатор**
```sql
and(
  exists(
    select 1
    from "tmp_anFilters_for_documentSearch" as an
      join comdoc."Route" as r on r."DocCode" = t."VCode" and r."DocType" = t."TypeName"
    where an."id" = 'Initiator'
      and r."Initiator" = an."value"
  )
)
```

**StageUser - Участник маршрута**
```sql
and 
  exists(
    select 1
    from "tmp_anFilters_for_documentSearch" as an
      join comdoc."Route" as r on r."DocCode" = t."VCode" and r."DocType" = t."TypeName"
	  join comdoc."RouteStage" as s on s."PCode" = r."VCode"
	  join comdoc."StageItem" as i on i."PCode" = s."VCode"
    where an."id" = 'StageUser'
      and r."RouteStatus" NOT IN (4)
      and i."StageUser" = an."value"
  ) 

```

**EmpowermentSubject - Полномочия**
```sql
and 
  exists(
    select 1
	from "tmp_anFilters_for_documentSearch" as an
	  join dfd."EmpowermentSubjectDetail" as esd on esd."PCode" = t."VCode"
          JOIN dfd."EmpowermentSubject" AS s ON esd."Subject" = s."VCode"
	where an."id" = 'EmpowermentSubject'
	  and t."TypeName" = 'EmpowermentConstructor'
	  and s."VCode" = an."value"::bigint
  )
```

**SignatoryUser - Работник**
```sql
and(
  exists(
    select 1
    from "tmp_anFilters_for_documentSearch" as an
      join comdoc."Route" as r on r."DocCode" = t."VCode" and r."DocType" = t."TypeName"
    where an."id" = 'SignatoryUser'
      and r."DocType" = 'EmployeeStatement'
      and r."Initiator" = an."value"
  ) or exists(
    select 1
    from "tmp_anFilters_for_documentSearch" as an
      join comdoc."Route" as r on r."DocCode" = t."VCode" and r."DocType" = t."TypeName"
	  join comdoc."RouteStage" as s on s."PCode" = r."VCode"
	  join comdoc."StageItem" as i on i."PCode" = s."VCode"
    where an."id" = 'SignatoryUser'
      and r."DocType" = 'LND'
	  AND r."RouteStatus" NOT IN(4)
	  AND s."IsMarked" IS NOT true
	  AND COALESCE(i."DocumentAction", 0) IN (20, 30)
      and i."StageUser" = an."value"
  ) or exists(
    select 1
	from "tmp_anFilters_for_documentSearch" as an
	  join comdoc."ReadListItem" as r on r."DocCode" = t."VCode" and r."DocType" = t."TypeName"
	where an."id" = 'SignatoryUser'
	  and r."DocType" = 'LND'
	  and r."DocflowUser" = an."value"
  ) or exists(
    select 1
	from "tmp_anFilters_for_documentSearch" as an
	  join dfd."EmpowermentWorkerDetail" as ewd on ewd."PCode" = t."VCode"
          JOIN rp."RP_Person" AS p ON ewd."PersonId" = p."VCode"
          JOIN rp."RP_PersonContact" AS pc on p."VCode" = pc."Pcode"
	where an."id" = 'SignatoryUser'
	  and t."TypeName" = 'EmpowermentConstructor'
          and pc."IdTypeContact" = 6
	  and pc."Code" = an."value"
  ) 
)
```

**Filial - Организация**
```sql
and
  exists(
    select 1
    from "tmp_anFilters_for_documentSearch" as an
    where an."id" = 'Filial'
      and t."COrg"::text = an."value"
  )
```

**Subtype - Подтип**
```sql
and
  exists(
    select 1
    from "tmp_anFilters_for_documentSearch" as an
    where an."id" = 'Subtype'
      and t."DocumentSubtype"::text = an."value"::text
  )
``` -->

## Настройка документов

После заполнения справочника «Итоговые выборки поисковой системы» необходимо перейти в реестр "Настройка документов". В документе необходимо заполнить поля typeNameProperty, dateProperty и numberProperty соответствующими им наименованиями полей таблицы: типа документа, даты документа и номера документа. Также необходимо в поле "Итоги" выбрать одно из значений справочника «Итоговые выборки поисковой системы». После заполнения этих полей необходимо поставить галочку в поле FTS2 и обновить страницу, чтобы изменения вступили в силу.

![Настройка](media/DocflowDocumentForm.png)

<!-- ## Примеры настраиваемых выборок

### Настраиваемая выборка "Приложение"

| Код           | Наименование        | SQLScript                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ------------- | ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Contractor    | Контрагент          | and exists(<br>  select 1 from "tmp_anFilters_for_documentSearch" as an where an."id" = 'Contractor' and an."value" = cast(t."Contractor" as character varying)<br>)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Contract      | Договор             | and exists(<br>  select 1 from "tmp_anFilters_for_documentSearch" as an where an."id" = 'Contract' and an."value" = cast(t."Contract" as character varying)<br>)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| CUser         | Создатель документа | and exists(<br>  select 1 from "tmp_anFilters_for_documentSearch" as an where an."id" = 'CUser' and an."value" = cast(t."CUser" as character varying)<br>)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | -->
<!-- | Initiator     | Инициатор           | and(<br>    exists(<br>      select 1<br>      from "tmp_anFilters_for_documentSearch" as an<br>        join comdoc."Route" as r on r."DocCode" = t."VCode" and r."DocType" = t."TypeName"<br>      where an."id" = 'Initiator'<br>        and r."Initiator" = an."value"<br>    ))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| StageUser     | Участник маршрута   | and <br>        exists(<br>          select 1<br>          from "tmp_anFilters_for_documentSearch" as an<br>            join comdoc."Route" as r on r."DocCode" = t."VCode" and r."DocType" = t."TypeName"<br>	          join comdoc."RouteStage" as s on s."PCode" = r."VCode"<br>	          join comdoc."StageItem" as i on i."PCode" = s."VCode"<br>        where an."id" = 'StageUser'<br>          and r."RouteStatus" NOT IN (4)<br>          and i."StageUser" = an."value"<br>        )                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| SignatoryUser | Работник            | and(exists(    select 1    from "tmp_anFilters_for_documentSearch" as an      join comdoc."Route" as r on r."DocCode" = t."VCode" and r."DocType" = t."TypeName"    where an."id" = 'SignatoryUser'      and r."DocType" = 'EmployeeStatement'      and r."Initiator" = an."value"  ) or exists( select 1   from "tmp_anFilters_for_documentSearch" as an      join comdoc."Route" as r on r."DocCode" = t."VCode" and r."DocType" = t."TypeName"	  join comdoc."RouteStage" as s on s."PCode" = r."VCode"	  join comdoc."StageItem" as i on i."PCode" = s."VCode"    where an."id" = 'SignatoryUser'      and r."DocType" = 'LND'	  AND r."RouteStatus" NOT IN(4)	  AND s."IsMarked" IS NOT true	  AND COALESCE(i."DocumentAction", 0) IN (20, 30)      and i."StageUser" = an."value"  ) or exists(    select 1	from "tmp_anFilters_for_documentSearch" as an	  join comdoc."ReadListItem" as r on r."DocCode" = t."VCode" and r."DocType" = t."TypeName"	where an."id" = 'SignatoryUser'	  and r."DocType" = 'LND' and r."DocflowUser" = an."value"  ) or exists(    select 1	from tmp_anFilters_for_documentSearch" as an	  join dfd."EmpowermentWorkerDetail" as ewd on ewd."PCode" = t."VCode"          JOIN rp."RP_Person" AS p ON ewd."PersonId" = p."VCode"          JOIN rp."RP_PersonContact" AS pc on p."VCode" = pc."Pcode"	where an."id" = 'SignatoryUser'	  and t."TypeName" = 'EmpowermentConstructor'          and pc."IdTypeContact" = 6	  and pc."Code" = an."value"  ) ) | -->
<!-- 
**В левую часть указывается скрипт:**

```sql
SELECT t."VCode" AS "DocCode"
     , t."TypeName" AS "DocType"
     , :DateProperty AS "DocDate"
     , :NumberProperty AS "DocNumber"
     , t."Contractor" AS "ContractorId"
     , t."Contract" AS "ContractId"
     , t."VCode" AS "AddContractId"
     , t."Projects" AS "ProjectId"
FROM contract."AdditionalContract" as t
WHERE t."COrg" = _orgidparam
```

**В правую часть:**

```sql
SELECT t."VCode" AS "DocCode"
     , t."TypeName" AS "DocType"
     , :DateProperty AS "DocDate"
     , :NumberProperty AS "DocNumber"
     , NULL::text AS "DocName"
     , t."SubjectOfContract" AS "DocTheme"
     , 'Содержание' AS "DocDefinition"
:ItemSelect
FROM contract."AdditionalContract" as t
:ItemFrom
WHERE t."COrg" = _orgidparam
:ItemWhere
```

### Настраиваемая выборка "Заявка на выпуск сертификата ЭП"

| Код           | Наименование | SQLScript                                                                                                                                                             |
| ------------- | ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SignatoryUser | Работник     | "and exists(<br> select 1 from "tmp_anFilters_for_documentSearch" as an where an."id" = 'SignatoryUser' and an."value" = cast(t."DocflowUser" as character varying))" |

**В левую часть указывается скрипт:**

```sql
SELECT t."VCode" AS "DocCode"
     , t."TypeName" AS "DocType"
     , :DateProperty AS "DocDate"
     , :NumberProperty AS "DocNumber"
     , NULL::bigint AS "ContractorId"
     , NULL::bigint AS "ContractId"
     , NULL::bigint AS "AddContractId"
     , NULL::bigint AS "ProjectId"
FROM comdoc."ECPCertificateApplication" as t
WHERE t."COrg" = _orgidparam
```

**В правую часть:**

```sql
SELECT t."VCode" AS "DocCode"
     , t."TypeName" AS "DocType"
     , :DateProperty AS "DocDate"
     , :NumberProperty AS "DocNumber"
     , NULL::text AS "DocName"
     , NULL::text AS "DocTheme"
     , NULL::text AS "DocDefinition"
:ItemSelect
FROM comdoc."ECPCertificateApplication" as t
:ItemFrom
WHERE t."COrg" = _orgidparam
:ItemWhere
``` -->

<!-- ### Настраиваемая выборка "Канцелярия"

| Код        | Наименование        | SQLScript                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ---------- | ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Contractor | Контрагент          | and exists(<br>  select 1 from "tmp_anFilters_for_documentSearch" as an where an."id" = 'Contractor' and an."value" = cast(t."Contractor" as character varying)<br>)                                                                                                                                                                                                                                                                                                                            |
| Contract   | Договор             | and exists(<br>  select 1 from "tmp_anFilters_for_documentSearch" as an where an."id" = 'Contract' and an."value" = cast(t."Contract" as character varying)<br>)                                                                                                                                                                                                                                                                                                                                |
| CUser      | Создатель документа | and exists(<br>  select 1 from "tmp_anFilters_for_documentSearch" as an where an."id" = 'CUser' and an."value" = cast(t."CUser" as character varying)<br>)                                                                                                                                                                                                                                                                                                                                      |
| Initiator  | Инициатор           | and(<br>    exists(<br>      select 1<br>      from "tmp_anFilters_for_documentSearch" as an<br>        join comdoc."Route" as r on r."DocCode" = t."VCode" and r."DocType" = t."TypeName"<br>      where an."id" = 'Initiator'<br>        and r."Initiator" = an."value"<br>    ))                                                                                                                                                                                                             |
| StageUser  | Участник маршрута   | and <br>        exists(<br>          select 1<br>          from "tmp_anFilters_for_documentSearch" as an<br>            join comdoc."Route" as r on r."DocCode" = t."VCode" and r."DocType" = t."TypeName"<br>	          join comdoc."RouteStage" as s on s."PCode" = r."VCode"<br>	          join comdoc."StageItem" as i on i."PCode" = s."VCode"<br>        where an."id" = 'StageUser'<br>          and r."RouteStatus" NOT IN (4)<br>          and i."StageUser" = an."value"<br>        ) | -->
<!-- 
**В левую часть указывается скрипт:**

```sql
SELECT t."VCode" AS "DocCode"
     , t."TypeName" AS "DocType"
     , :DateProperty AS "DocDate"
     , :NumberProperty AS "DocNumber"
     , t."Contractor" AS "ContractorId"
     , t."VCode" AS "ContractId"
     , NULL::bigint AS "AddContractId"
     , t."Projects" AS "ProjectId"
FROM dfd."DocflowDocument" as t
WHERE t."COrg" = _orgidparam
```

**В правую часть:**

```sql
SELECT t."VCode" AS "DocCode"
     , t."TypeName" AS "DocType"
     , :DateProperty AS "DocDate"
     , :NumberProperty AS "DocNumber"
     , NULL::text AS "DocName"
     , NULL::text AS "DocTheme"
     , NULL::text AS "DocDefinition"
FROM dfd."DocflowDocument" as t
WHERE t."COrg" = _orgidparam
```  -->

## Автоматическое формирование отчета заявления с ЭП

На проекте возможно настроить автоматическое формирование отчета заявления с электронными подписями по завершению маршрута. Для этого в документе "Настройка учетной политики предприятия" нужно настроить константу **Интеграция с 1С с помощью сервиса ODATA** со значением 1

![Константа](media/constant.png)

По завершению маршрута в окно вложений заявления добавится печатная форма с ЭП. Архив с ЭП можно будет скачать по кнопке "Скачать архив с ЭП".

![Вложения](media/attachments.png)

Скачать архив с ЭП можно только когда в маршруте пройдены все этапы с действием "Подписан ЭП" и текущий этап 
не требует подписания документа. 

![Этапы](media/stages.png)

Архив скачается в папку "Загрузки" (Downloads).

![Загрузки](media/Downloads.png)

В архиве будут находиться: оригинал заявления, отчет по подписанию и файл с информацией о подписании данного документа по каждому сотруднику.

![Архив ЭП](media/arhiv.png)

## Настройка отчета без включения пропущенных этапов подписания

В проекте есть возможность не добавлять в отчет тех сотрудников, кто включен в маршрут через **ИЛИ** и **НЕ ПРОШЕЛ** этап подписания. 

![Статус пропущен](media/skipped.png)

Для этого в документе "Настройка учетной политики предприятия" нужно настроить константу **Скрывать участников маршрута без действий** со значением 1. 

![Константа2](media/constant2.png)

Результат сформированного отчета:

![Отчет маршрута](media/skippedPrint.png)