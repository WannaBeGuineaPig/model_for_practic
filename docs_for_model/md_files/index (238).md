# Настройка правил поиска для истории операций

## Описание

В данной форме настраиваются правила поиска документа для [истории операций](https://ecm-user-manuals.readthedocs.io/ru/latest/User%20manuals/%D0%98%D1%81%D1%82%D0%BE%D1%80%D0%B8%D1%8F%20%D0%BE%D0%BF%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D0%B9/)
Чтобы открыть данную форму необходимо в Меню в поисковой строке ввести - "Настройка правил поиска для истории операций". Для доступа к данному времени пользователю необходимо назначить роль **rulesforunifieddocumentreg_write**

## Работа с данной формой

## Вкладка "Настройки"

На данной вкладке задаются основные настройки поиска документов.

* **Не используется** - при включенной функции данная настройка не будет отображаться в журнале состояния документов.

![Alt text](media/image-2.png)

![Alt text](media/image-1.png)

* **№ / Наименование** - указывается наименование настройки для отображения в журнале состояния документов.

![Alt text](media/image-3.png)

![Alt text](media/image-4.png)

* **Служебное наименование** - указывается служебное наименование по которому фильтруется реестр документов. Служебное наименование должно быть **уникальным** в системе.

![Alt text](media/image-5.png)

**Использовать по умолчанию** - при включенной опции данный запрос будет заполняться автоматически в поле **"Что найти"**: 

![Alt text](media/image-6.png)

![Alt text](media/image-7.png)

<!-- ## Вкладка "Запрос"

В данном блоке указывается часть с динамическим запросом, содержащим непосредственно запроса для отображения документов.

Примеры запросов:

### Документы с моим участием

```sql
	insert into "#tmp_finresult"(   "VCode", "TypeName", "RDate", "DocumentNumber","DocumentSubtype","routeId", "attr", "Operation")
	select   t."VCode", t."TypeName", t."RDate", t."DocumentNumber",t."DocumentSubtype",t."routeId", 
(case when not exists (select 1 from comdoc."Route" AS r where r."DocCode" = t."VCode" AND r."DocType" = t."TypeName") 
	                         then 'Маршрут не создан'
							 when t."RouteStatus" = 2 then 'Идет согласование. Текущие участники: ' || rst."CurrentDocflowUser" 
							 when t."RouteStatus" = 3 then 'Согласование завершено'
							 when  exists (select 1 from comdoc."Route" AS r where r."DocCode" = t."VCode" AND r."DocType" = t."TypeName" and r."RouteStatus" = 4)
								and not exists (select 1 from comdoc."Route" AS r where r."DocCode" = t."VCode" AND r."DocType" = t."TypeName" and r."RouteStatus" in(2,3)) then 'Маршрут согласования отменен'
	                        end::text ) ||' '||
 (select string_agg(dca."Name" || ':' || (case 
				when coalesce(dca."AttributeType",'')  = 'string' and  coalesce(atr."Value",'') <> '' then atr."Value"
				when coalesce(dca."AttributeType",'')  = 'string' and coalesce(atr."Value",'') = '' then ' '
				
				when coalesce(dca."AttributeType",'')  = 'bigint' and atr."BigIntValue" is not null then cast(atr."BigIntValue" as varchar(255))
				when coalesce(dca."AttributeType",'')  = 'bigint' and atr."BigIntValue" is null then ' '
				
				when coalesce(dca."AttributeType",'')  = 'string' and atr."BigIntValue" is not null then cast(atr."BigIntValue" as varchar(255))
				when coalesce(dca."AttributeType",'')  = 'string' and atr."BigIntValue" is null then ' '

				when coalesce(dca."AttributeType",'') = 'Base.Unispr' and atr."BigIntValue" is null and coalesce(atr."Value",'') = '' then ' '
				when coalesce(dca."AttributeType",'') = 'Base.Unispr' and atr."BigIntValue" is not null and coalesce(atr."Value",'') <> '' then coalesce(atr."Value",' ')

				when coalesce(dca."AttributeType",'') = 'Base.Post' and atr."BigIntValue" is null and coalesce(atr."Value",'') = '' then ' '
				when coalesce(dca."AttributeType",'') = 'Base.Post' and atr."BigIntValue" is not null and coalesce(atr."Value",'') <> '' then coalesce(atr."Value",' ')

				when coalesce(dca."AttributeType",'') = 'Base.RP_Worker' and atr."BigIntValue" is null and coalesce(atr."Value",'') = '' then ' '
				when coalesce(dca."AttributeType",'') = 'Base.RP_Worker' and atr."BigIntValue" is not null and coalesce(atr."Value",'') <> '' then coalesce(atr."Value",' ')

				when coalesce(dca."AttributeType",'') = 'Base.Contract' and atr."BigIntValue" is null and coalesce(atr."Value",'') = '' then ' '
				when coalesce(dca."AttributeType",'') = 'Base.Contract' and atr."BigIntValue" is not null and coalesce(atr."Value",'') <> '' then coalesce(atr."Value",' ')

				when coalesce(dca."AttributeType",'') = 'Base.Contractor' and atr."BigIntValue" is null and coalesce(atr."Value",'') = '' then ' '
				when coalesce(dca."AttributeType",'') = 'Base.Contractor' and atr."BigIntValue" is not null and coalesce(atr."Value",'') <> '' then coalesce(atr."Value",' ')

				when coalesce(dca."AttributeType",'') = 'Base.Department' and atr."BigIntValue" is null and coalesce(atr."Value",'') = '' then ' '
				when coalesce(dca."AttributeType",'') = 'Base.Department' and atr."BigIntValue" is not null and coalesce(atr."Value",'') <> '' then coalesce(atr."Value",' ')

				when coalesce(dca."AttributeType",'') = 'money' and atr."MoneyValue"  is not null then cast(atr."MoneyValue" as varchar(255))
				when coalesce(dca."AttributeType",'') = 'money' and atr."MoneyValue"  is  null then ' '

				when coalesce(dca."AttributeType",'') = 'Date' and atr."DateValue"  is not null then to_char(atr."DateValue", 'DD.MM.YYYY')
				when coalesce(dca."AttributeType",'') = 'Date' and atr."DateValue"  is null then ' '

        		when coalesce(dca."AttributeType",'') = 'DateTime' and atr."DateTimeValue"  is not null then to_char(atr."DateValue", 'DD.MM.YYYY')
				when coalesce(dca."AttributeType",'') = 'DateTime' and atr."DateTimeValue"  is null then ' '
			
				when coalesce(dca."AttributeType",'')  = 'double' and atr."DoubleValue"  is not null then cast(atr."DoubleValue" as varchar(255))
				when coalesce(dca."AttributeType",'')  = 'double' and atr."DoubleValue"  is null then ' '

				when coalesce(dca."AttributeType",'')  = 'ServiceWord' and coalesce(atr."Value",'') <> '' then coalesce(atr."Value",' ') 
				when coalesce(dca."AttributeType",'')  = 'ServiceWord' and coalesce(atr."Value",'') = '' then ' '

       	 		when coalesce(dca."AttributeType",'')  = 'bool' and coalesce("BigIntValue"::integer,0) = 0 then substring(coalesce("Value",'|'),	position('|' in coalesce("Value",'|'))+1,char_length(coalesce("Value",'|')))
				when coalesce(dca."AttributeType",'')  = 'bool' and coalesce("BigIntValue"::integer,0) = 1 then substring(coalesce("Value",'|'),0,	position('|' in coalesce("Value",'|')))
								
			end), '; ') AS "x"
				    from   dfd."DocumentAdditionalAttribute" atr 
          			    join dfd."DocumentCategoryAttributeType" dca on atr."CategoryAttributeType" = dca."VCode"
				    where  t."VCode" = atr."PCode" ) ,
        (case when t."TypeName" = 'LND' then 'Поступил ЛНА на ознакомление'
           when t."TypeName" = 'DocumentForSigning' then 'Поступил из 1С документ на подписание'
          when t."TypeName" = 'EmployeeStatement' then 'Создано ' || ds."Name" ||' и отправлено на согласование'
          else 'Поступил документ на подписание'
        end)
	  from "#tmp_preresult" t
  left join dfd."DocumentSubtype" ds on ds."VCode" = t."DocumentSubtype"
 LEFT JOIN LATERAL comdoc."getDocRouteCurrentStatus"(t."VCode", t."TypeName") AS rst ON true ;
 ```

### Документы с моим участием

```sql
	insert into "#tmp_finresult"(   "VCode", "TypeName", "RDate", "DocumentNumber","DocumentSubtype","routeId", "attr", "Operation")
	select  t."VCode", t."TypeName", t."RDate", t."DocumentNumber",t."DocumentSubtype",t."routeId",

(case when not exists (select 1 from comdoc."Route" AS r where r."DocCode" = t."VCode" AND r."DocType" = t."TypeName") 
	                         then 'Маршрут не создан'
							 when t."RouteStatus" = 2 then 'Идет согласование. Текущие участники: ' || rst."CurrentDocflowUser" 
							 when t."RouteStatus" = 3 then 'Согласование завершено'
							 when  exists (select 1 from comdoc."Route" AS r where r."DocCode" = t."VCode" AND r."DocType" = t."TypeName" and r."RouteStatus" = 4)
								and not exists (select 1 from comdoc."Route" AS r where r."DocCode" = t."VCode" AND r."DocType" = t."TypeName" and r."RouteStatus" in(2,3)) then 'Маршрут согласования отменен'
	                        end::text ) ||' '||
 (select string_agg(dca."Name" || ':' || (case 
				when coalesce(dca."AttributeType",'')  = 'string' and  coalesce(atr."Value",'') <> '' then atr."Value"
				when coalesce(dca."AttributeType",'')  = 'string' and coalesce(atr."Value",'') = '' then ' '
				
				when coalesce(dca."AttributeType",'')  = 'bigint' and atr."BigIntValue" is not null then cast(atr."BigIntValue" as varchar(255))
				when coalesce(dca."AttributeType",'')  = 'bigint' and atr."BigIntValue" is null then ' '
				
				when coalesce(dca."AttributeType",'')  = 'string' and atr."BigIntValue" is not null then cast(atr."BigIntValue" as varchar(255))
				when coalesce(dca."AttributeType",'')  = 'string' and atr."BigIntValue" is null then ' '

				when coalesce(dca."AttributeType",'') = 'Base.Unispr' and atr."BigIntValue" is null and coalesce(atr."Value",'') = '' then ' '
				when coalesce(dca."AttributeType",'') = 'Base.Unispr' and atr."BigIntValue" is not null and coalesce(atr."Value",'') <> '' then coalesce(atr."Value",' ')

				when coalesce(dca."AttributeType",'') = 'Base.Post' and atr."BigIntValue" is null and coalesce(atr."Value",'') = '' then ' '
				when coalesce(dca."AttributeType",'') = 'Base.Post' and atr."BigIntValue" is not null and coalesce(atr."Value",'') <> '' then coalesce(atr."Value",' ')

				when coalesce(dca."AttributeType",'') = 'Base.RP_Worker' and atr."BigIntValue" is null and coalesce(atr."Value",'') = '' then ' '
				when coalesce(dca."AttributeType",'') = 'Base.RP_Worker' and atr."BigIntValue" is not null and coalesce(atr."Value",'') <> '' then coalesce(atr."Value",' ')

				when coalesce(dca."AttributeType",'') = 'Base.Contract' and atr."BigIntValue" is null and coalesce(atr."Value",'') = '' then ' '
				when coalesce(dca."AttributeType",'') = 'Base.Contract' and atr."BigIntValue" is not null and coalesce(atr."Value",'') <> '' then coalesce(atr."Value",' ')

				when coalesce(dca."AttributeType",'') = 'Base.Contractor' and atr."BigIntValue" is null and coalesce(atr."Value",'') = '' then ' '
				when coalesce(dca."AttributeType",'') = 'Base.Contractor' and atr."BigIntValue" is not null and coalesce(atr."Value",'') <> '' then coalesce(atr."Value",' ')

				when coalesce(dca."AttributeType",'') = 'Base.Department' and atr."BigIntValue" is null and coalesce(atr."Value",'') = '' then ' '
				when coalesce(dca."AttributeType",'') = 'Base.Department' and atr."BigIntValue" is not null and coalesce(atr."Value",'') <> '' then coalesce(atr."Value",' ')

				when coalesce(dca."AttributeType",'') = 'money' and atr."MoneyValue"  is not null then cast(atr."MoneyValue" as varchar(255))
				when coalesce(dca."AttributeType",'') = 'money' and atr."MoneyValue"  is  null then ' '

				when coalesce(dca."AttributeType",'') = 'Date' and atr."DateValue"  is not null then to_char(atr."DateValue", 'DD.MM.YYYY')
				when coalesce(dca."AttributeType",'') = 'Date' and atr."DateValue"  is null then ' '

        		when coalesce(dca."AttributeType",'') = 'DateTime' and atr."DateTimeValue"  is not null then to_char(atr."DateValue", 'DD.MM.YYYY')
				when coalesce(dca."AttributeType",'') = 'DateTime' and atr."DateTimeValue"  is null then ' '
			
				when coalesce(dca."AttributeType",'')  = 'double' and atr."DoubleValue"  is not null then cast(atr."DoubleValue" as varchar(255))
				when coalesce(dca."AttributeType",'')  = 'double' and atr."DoubleValue"  is null then ' '

				when coalesce(dca."AttributeType",'')  = 'ServiceWord' and coalesce(atr."Value",'') <> '' then coalesce(atr."Value",' ') 
				when coalesce(dca."AttributeType",'')  = 'ServiceWord' and coalesce(atr."Value",'') = '' then ' '

       	 		when coalesce(dca."AttributeType",'')  = 'bool' and coalesce("BigIntValue"::integer,0) = 0 then substring(coalesce("Value",'|'),	position('|' in coalesce("Value",'|'))+1,char_length(coalesce("Value",'|')))
				when coalesce(dca."AttributeType",'')  = 'bool' and coalesce("BigIntValue"::integer,0) = 1 then substring(coalesce("Value",'|'),0,	position('|' in coalesce("Value",'|')))
								
			end), '; ') AS "x"
				    from   dfd."DocumentAdditionalAttribute" atr 
          			    join dfd."DocumentCategoryAttributeType" dca on atr."CategoryAttributeType" = dca."VCode"
				    where  t."VCode" = atr."PCode" ) ,

          (case when t."TypeName" = 'LND' then 'Поступил ЛНА на ознакомление'
           when t."TypeName" = 'DocumentForSigning' then 'Поступил из 1С документ на подписание'
          when t."TypeName" = 'EmployeeStatement' then 'Создано ' || ds."Name" ||' и отправлено на согласование'
          else 'Поступил документ на подписание'
        end)
	  from "#tmp_preresult" t
          LEFT JOIN LATERAL comdoc."getDocRouteCurrentStatus"(t."VCode", t."TypeName") AS rst ON true 
        left join dfd."DocumentSubtype" ds on ds."VCode" = t."DocumentSubtype"
	  where t."TypeName" = 'EmployeeStatement'
        and t."CUser" = t."StageUser";
```

### Мои справки

```sql
	insert into "#tmp_finresult"(   "VCode", "TypeName", "RDate", "DocumentNumber","DocumentSubtype","routeId", "attr", "Operation")
	select  t."VCode", t."TypeName", t."RDate", t."DocumentNumber",t."DocumentSubtype",t."routeId",

(case when not exists (select 1 from comdoc."Route" AS r where r."DocCode" = t."VCode" AND r."DocType" = t."TypeName") 
	                         then 'Маршрут не создан'
							 when t."RouteStatus" = 2 then 'Идет согласование. Текущие участники: ' || rst."CurrentDocflowUser" 
							 when t."RouteStatus" = 3 then 'Согласование завершено'
							 when  exists (select 1 from comdoc."Route" AS r where r."DocCode" = t."VCode" AND r."DocType" = t."TypeName" and r."RouteStatus" = 4)
								and not exists (select 1 from comdoc."Route" AS r where r."DocCode" = t."VCode" AND r."DocType" = t."TypeName" and r."RouteStatus" in(2,3)) then 'Маршрут согласования отменен'
	                        end::text ) ||' '||
 (select string_agg(dca."Name" || ':' || (case 
				when coalesce(dca."AttributeType",'')  = 'string' and  coalesce(atr."Value",'') <> '' then atr."Value"
				when coalesce(dca."AttributeType",'')  = 'string' and coalesce(atr."Value",'') = '' then ' '
				
				when coalesce(dca."AttributeType",'')  = 'bigint' and atr."BigIntValue" is not null then cast(atr."BigIntValue" as varchar(255))
				when coalesce(dca."AttributeType",'')  = 'bigint' and atr."BigIntValue" is null then ' '
				
				when coalesce(dca."AttributeType",'')  = 'string' and atr."BigIntValue" is not null then cast(atr."BigIntValue" as varchar(255))
				when coalesce(dca."AttributeType",'')  = 'string' and atr."BigIntValue" is null then ' '

				when coalesce(dca."AttributeType",'') = 'Base.Unispr' and atr."BigIntValue" is null and coalesce(atr."Value",'') = '' then ' '
				when coalesce(dca."AttributeType",'') = 'Base.Unispr' and atr."BigIntValue" is not null and coalesce(atr."Value",'') <> '' then coalesce(atr."Value",' ')

				when coalesce(dca."AttributeType",'') = 'Base.Post' and atr."BigIntValue" is null and coalesce(atr."Value",'') = '' then ' '
				when coalesce(dca."AttributeType",'') = 'Base.Post' and atr."BigIntValue" is not null and coalesce(atr."Value",'') <> '' then coalesce(atr."Value",' ')

				when coalesce(dca."AttributeType",'') = 'Base.RP_Worker' and atr."BigIntValue" is null and coalesce(atr."Value",'') = '' then ' '
				when coalesce(dca."AttributeType",'') = 'Base.RP_Worker' and atr."BigIntValue" is not null and coalesce(atr."Value",'') <> '' then coalesce(atr."Value",' ')

				when coalesce(dca."AttributeType",'') = 'Base.Contract' and atr."BigIntValue" is null and coalesce(atr."Value",'') = '' then ' '
				when coalesce(dca."AttributeType",'') = 'Base.Contract' and atr."BigIntValue" is not null and coalesce(atr."Value",'') <> '' then coalesce(atr."Value",' ')

				when coalesce(dca."AttributeType",'') = 'Base.Contractor' and atr."BigIntValue" is null and coalesce(atr."Value",'') = '' then ' '
				when coalesce(dca."AttributeType",'') = 'Base.Contractor' and atr."BigIntValue" is not null and coalesce(atr."Value",'') <> '' then coalesce(atr."Value",' ')

				when coalesce(dca."AttributeType",'') = 'Base.Department' and atr."BigIntValue" is null and coalesce(atr."Value",'') = '' then ' '
				when coalesce(dca."AttributeType",'') = 'Base.Department' and atr."BigIntValue" is not null and coalesce(atr."Value",'') <> '' then coalesce(atr."Value",' ')

				when coalesce(dca."AttributeType",'') = 'money' and atr."MoneyValue"  is not null then cast(atr."MoneyValue" as varchar(255))
				when coalesce(dca."AttributeType",'') = 'money' and atr."MoneyValue"  is  null then ' '

				when coalesce(dca."AttributeType",'') = 'Date' and atr."DateValue"  is not null then to_char(atr."DateValue", 'DD.MM.YYYY')
				when coalesce(dca."AttributeType",'') = 'Date' and atr."DateValue"  is null then ' '

        		when coalesce(dca."AttributeType",'') = 'DateTime' and atr."DateTimeValue"  is not null then to_char(atr."DateValue", 'DD.MM.YYYY')
				when coalesce(dca."AttributeType",'') = 'DateTime' and atr."DateTimeValue"  is null then ' '
			
				when coalesce(dca."AttributeType",'')  = 'double' and atr."DoubleValue"  is not null then cast(atr."DoubleValue" as varchar(255))
				when coalesce(dca."AttributeType",'')  = 'double' and atr."DoubleValue"  is null then ' '

				when coalesce(dca."AttributeType",'')  = 'ServiceWord' and coalesce(atr."Value",'') <> '' then coalesce(atr."Value",' ') 
				when coalesce(dca."AttributeType",'')  = 'ServiceWord' and coalesce(atr."Value",'') = '' then ' '

       	 		when coalesce(dca."AttributeType",'')  = 'bool' and coalesce("BigIntValue"::integer,0) = 0 then substring(coalesce("Value",'|'),	position('|' in coalesce("Value",'|'))+1,char_length(coalesce("Value",'|')))
				when coalesce(dca."AttributeType",'')  = 'bool' and coalesce("BigIntValue"::integer,0) = 1 then substring(coalesce("Value",'|'),0,	position('|' in coalesce("Value",'|')))
								
			end), '; ') AS "x"
				    from   dfd."DocumentAdditionalAttribute" atr 
          			    join dfd."DocumentCategoryAttributeType" dca on atr."CategoryAttributeType" = dca."VCode"
				    where  t."VCode" = atr."PCode" ) ,

          ('Заказ справки 2НДФЛ')
	  from "#tmp_preresult" t
          LEFT JOIN LATERAL comdoc."getDocRouteCurrentStatus"(t."VCode", t."TypeName") AS rst ON true 
          left join dfd."DocumentSubtype" ds on ds."VCode" = t."DocumentSubtype"
	  where (t."TypeName" = 'EmployeeStatement'    and t."DocumentSubtype" = 39) OR (t."TypeName" = 'DocumentForSigning'    and t."DocumentSubtype" = 40);
```

### Инструкции и положения по работе

```sql
	insert into "#tmp_finresult"(   "VCode", "TypeName", "RDate", "DocumentNumber","DocumentSubtype", "attr", "Operation")
	select   t."VCode", t."TypeName", t."RDate", t."DocumentNumber",t."DocumentSubtype",
(case when not exists (select 1 from comdoc."Route" AS r where r."DocCode" = t."VCode" AND r."DocType" = t."TypeName") 
	                         then 'Маршрут не создан'
							 when t."RouteStatus" = 2 then 'Идет согласование. Текущие участники: ' || rst."CurrentDocflowUser" 
							 when t."RouteStatus" = 3 then 'Согласование завершено'
							 when  exists (select 1 from comdoc."Route" AS r where r."DocCode" = t."VCode" AND r."DocType" = t."TypeName" and r."RouteStatus" = 4)
								and not exists (select 1 from comdoc."Route" AS r where r."DocCode" = t."VCode" AND r."DocType" = t."TypeName" and r."RouteStatus" in(2,3)) then 'Маршрут согласования отменен'
	                        end::text ) ||' '||
 (select string_agg(dca."Name" || ':' || (case 
				when coalesce(dca."AttributeType",'')  = 'string' and  coalesce(atr."Value",'') <> '' then atr."Value"
				when coalesce(dca."AttributeType",'')  = 'string' and coalesce(atr."Value",'') = '' then ' '
				
				when coalesce(dca."AttributeType",'')  = 'bigint' and atr."BigIntValue" is not null then cast(atr."BigIntValue" as varchar(255))
				when coalesce(dca."AttributeType",'')  = 'bigint' and atr."BigIntValue" is null then ' '
				
				when coalesce(dca."AttributeType",'')  = 'string' and atr."BigIntValue" is not null then cast(atr."BigIntValue" as varchar(255))
				when coalesce(dca."AttributeType",'')  = 'string' and atr."BigIntValue" is null then ' '

				when coalesce(dca."AttributeType",'') = 'Base.Unispr' and atr."BigIntValue" is null and coalesce(atr."Value",'') = '' then ' '
				when coalesce(dca."AttributeType",'') = 'Base.Unispr' and atr."BigIntValue" is not null and coalesce(atr."Value",'') <> '' then coalesce(atr."Value",' ')

				when coalesce(dca."AttributeType",'') = 'Base.Post' and atr."BigIntValue" is null and coalesce(atr."Value",'') = '' then ' '
				when coalesce(dca."AttributeType",'') = 'Base.Post' and atr."BigIntValue" is not null and coalesce(atr."Value",'') <> '' then coalesce(atr."Value",' ')

				when coalesce(dca."AttributeType",'') = 'Base.RP_Worker' and atr."BigIntValue" is null and coalesce(atr."Value",'') = '' then ' '
				when coalesce(dca."AttributeType",'') = 'Base.RP_Worker' and atr."BigIntValue" is not null and coalesce(atr."Value",'') <> '' then coalesce(atr."Value",' ')

				when coalesce(dca."AttributeType",'') = 'Base.Contract' and atr."BigIntValue" is null and coalesce(atr."Value",'') = '' then ' '
				when coalesce(dca."AttributeType",'') = 'Base.Contract' and atr."BigIntValue" is not null and coalesce(atr."Value",'') <> '' then coalesce(atr."Value",' ')

				when coalesce(dca."AttributeType",'') = 'Base.Contractor' and atr."BigIntValue" is null and coalesce(atr."Value",'') = '' then ' '
				when coalesce(dca."AttributeType",'') = 'Base.Contractor' and atr."BigIntValue" is not null and coalesce(atr."Value",'') <> '' then coalesce(atr."Value",' ')

				when coalesce(dca."AttributeType",'') = 'Base.Department' and atr."BigIntValue" is null and coalesce(atr."Value",'') = '' then ' '
				when coalesce(dca."AttributeType",'') = 'Base.Department' and atr."BigIntValue" is not null and coalesce(atr."Value",'') <> '' then coalesce(atr."Value",' ')

				when coalesce(dca."AttributeType",'') = 'money' and atr."MoneyValue"  is not null then cast(atr."MoneyValue" as varchar(255))
				when coalesce(dca."AttributeType",'') = 'money' and atr."MoneyValue"  is  null then ' '

				when coalesce(dca."AttributeType",'') = 'Date' and atr."DateValue"  is not null then to_char(atr."DateValue", 'DD.MM.YYYY')
				when coalesce(dca."AttributeType",'') = 'Date' and atr."DateValue"  is null then ' '

        		when coalesce(dca."AttributeType",'') = 'DateTime' and atr."DateTimeValue"  is not null then to_char(atr."DateValue", 'DD.MM.YYYY')
				when coalesce(dca."AttributeType",'') = 'DateTime' and atr."DateTimeValue"  is null then ' '
			
				when coalesce(dca."AttributeType",'')  = 'double' and atr."DoubleValue"  is not null then cast(atr."DoubleValue" as varchar(255))
				when coalesce(dca."AttributeType",'')  = 'double' and atr."DoubleValue"  is null then ' '

				when coalesce(dca."AttributeType",'')  = 'ServiceWord' and coalesce(atr."Value",'') <> '' then coalesce(atr."Value",' ') 
				when coalesce(dca."AttributeType",'')  = 'ServiceWord' and coalesce(atr."Value",'') = '' then ' '

       	 		when coalesce(dca."AttributeType",'')  = 'bool' and coalesce("BigIntValue"::integer,0) = 0 then substring(coalesce("Value",'|'),	position('|' in coalesce("Value",'|'))+1,char_length(coalesce("Value",'|')))
				when coalesce(dca."AttributeType",'')  = 'bool' and coalesce("BigIntValue"::integer,0) = 1 then substring(coalesce("Value",'|'),0,	position('|' in coalesce("Value",'|')))
								
			end), '; ') AS "x"
				    from   dfd."DocumentAdditionalAttribute" atr 
          			    join dfd."DocumentCategoryAttributeType" dca on atr."CategoryAttributeType" = dca."VCode"
				    where  t."VCode" = atr."PCode" ) ,
        (case when t."TypeName" = 'LND' then 'Поступил ЛНА на ознакомление'
           when t."TypeName" = 'DocumentForSigning' then 'Поступил из 1С документ на подписание'
          when t."TypeName" = 'EmployeeStatement' then 'Создано ' || ds."Name" ||' и отправлено на согласование'
          else 'Поступил документ на подписание'
        end)
	  from "#tmp_preresult" t
  LEFT JOIN LATERAL comdoc."getDocRouteCurrentStatus"(t."VCode", t."TypeName") AS rst ON true 
        left join dfd."DocumentSubtype" ds on ds."VCode" = t."DocumentSubtype"
	  where t."TypeName" = 'LND';
```

### Все мои документы (заявления + ЛНА)

```sql
	insert into "#tmp_finresult"(   "VCode", "TypeName", "RDate", "DocumentNumber","DocumentSubtype","routeId", "attr", "Operation")
	select   t."VCode", t."TypeName", t."RDate", t."DocumentNumber",t."DocumentSubtype",t."routeId", 
(case when not exists (select 1 from comdoc."Route" AS r where r."DocCode" = t."VCode" AND r."DocType" = t."TypeName") 
	                         then 'Маршрут не создан'
							 when t."RouteStatus" = 2 then 'Идет согласование. Текущие участники: ' || rst."CurrentDocflowUser" 
							 when t."RouteStatus" = 3 then 'Согласование завершено'
							 when  exists (select 1 from comdoc."Route" AS r where r."DocCode" = t."VCode" AND r."DocType" = t."TypeName" and r."RouteStatus" = 4)
								and not exists (select 1 from comdoc."Route" AS r where r."DocCode" = t."VCode" AND r."DocType" = t."TypeName" and r."RouteStatus" in(2,3)) then 'Маршрут согласования отменен'
	                        end::text ) ||' '||
 (select string_agg(dca."Name" || ':' || (case 
				when coalesce(dca."AttributeType",'')  = 'string' and  coalesce(atr."Value",'') <> '' then atr."Value"
				when coalesce(dca."AttributeType",'')  = 'string' and coalesce(atr."Value",'') = '' then ' '
				
				when coalesce(dca."AttributeType",'')  = 'bigint' and atr."BigIntValue" is not null then cast(atr."BigIntValue" as varchar(255))
				when coalesce(dca."AttributeType",'')  = 'bigint' and atr."BigIntValue" is null then ' '
				
				when coalesce(dca."AttributeType",'')  = 'string' and atr."BigIntValue" is not null then cast(atr."BigIntValue" as varchar(255))
				when coalesce(dca."AttributeType",'')  = 'string' and atr."BigIntValue" is null then ' '

				when coalesce(dca."AttributeType",'') = 'Base.Unispr' and atr."BigIntValue" is null and coalesce(atr."Value",'') = '' then ' '
				when coalesce(dca."AttributeType",'') = 'Base.Unispr' and atr."BigIntValue" is not null and coalesce(atr."Value",'') <> '' then coalesce(atr."Value",' ')

				when coalesce(dca."AttributeType",'') = 'Base.Post' and atr."BigIntValue" is null and coalesce(atr."Value",'') = '' then ' '
				when coalesce(dca."AttributeType",'') = 'Base.Post' and atr."BigIntValue" is not null and coalesce(atr."Value",'') <> '' then coalesce(atr."Value",' ')

				when coalesce(dca."AttributeType",'') = 'Base.RP_Worker' and atr."BigIntValue" is null and coalesce(atr."Value",'') = '' then ' '
				when coalesce(dca."AttributeType",'') = 'Base.RP_Worker' and atr."BigIntValue" is not null and coalesce(atr."Value",'') <> '' then coalesce(atr."Value",' ')

				when coalesce(dca."AttributeType",'') = 'Base.Contract' and atr."BigIntValue" is null and coalesce(atr."Value",'') = '' then ' '
				when coalesce(dca."AttributeType",'') = 'Base.Contract' and atr."BigIntValue" is not null and coalesce(atr."Value",'') <> '' then coalesce(atr."Value",' ')

				when coalesce(dca."AttributeType",'') = 'Base.Contractor' and atr."BigIntValue" is null and coalesce(atr."Value",'') = '' then ' '
				when coalesce(dca."AttributeType",'') = 'Base.Contractor' and atr."BigIntValue" is not null and coalesce(atr."Value",'') <> '' then coalesce(atr."Value",' ')

				when coalesce(dca."AttributeType",'') = 'Base.Department' and atr."BigIntValue" is null and coalesce(atr."Value",'') = '' then ' '
				when coalesce(dca."AttributeType",'') = 'Base.Department' and atr."BigIntValue" is not null and coalesce(atr."Value",'') <> '' then coalesce(atr."Value",' ')

				when coalesce(dca."AttributeType",'') = 'money' and atr."MoneyValue"  is not null then cast(atr."MoneyValue" as varchar(255))
				when coalesce(dca."AttributeType",'') = 'money' and atr."MoneyValue"  is  null then ' '

				when coalesce(dca."AttributeType",'') = 'Date' and atr."DateValue"  is not null then to_char(atr."DateValue", 'DD.MM.YYYY')
				when coalesce(dca."AttributeType",'') = 'Date' and atr."DateValue"  is null then ' '

        		when coalesce(dca."AttributeType",'') = 'DateTime' and atr."DateTimeValue"  is not null then to_char(atr."DateValue", 'DD.MM.YYYY')
				when coalesce(dca."AttributeType",'') = 'DateTime' and atr."DateTimeValue"  is null then ' '
			
				when coalesce(dca."AttributeType",'')  = 'double' and atr."DoubleValue"  is not null then cast(atr."DoubleValue" as varchar(255))
				when coalesce(dca."AttributeType",'')  = 'double' and atr."DoubleValue"  is null then ' '

				when coalesce(dca."AttributeType",'')  = 'ServiceWord' and coalesce(atr."Value",'') <> '' then coalesce(atr."Value",' ') 
				when coalesce(dca."AttributeType",'')  = 'ServiceWord' and coalesce(atr."Value",'') = '' then ' '

       	 		when coalesce(dca."AttributeType",'')  = 'bool' and coalesce("BigIntValue"::integer,0) = 0 then substring(coalesce("Value",'|'),	position('|' in coalesce("Value",'|'))+1,char_length(coalesce("Value",'|')))
				when coalesce(dca."AttributeType",'')  = 'bool' and coalesce("BigIntValue"::integer,0) = 1 then substring(coalesce("Value",'|'),0,	position('|' in coalesce("Value",'|')))
								
			end), '; ') AS "x"
				    from   dfd."DocumentAdditionalAttribute" atr 
          			    join dfd."DocumentCategoryAttributeType" dca on atr."CategoryAttributeType" = dca."VCode"
				    where  t."VCode" = atr."PCode" ) ,
        (case when t."TypeName" = 'LND' then 'Поступил ЛНА на ознакомление'
           when t."TypeName" = 'DocumentForSigning' then 'Поступил из 1С документ на подписание'
          when t."TypeName" = 'EmployeeStatement' then 'Создано ' || ds."Name" ||' и отправлено на согласование'
          else 'Поступил документ на подписание'
        end)
	  from "#tmp_preresult" t
  left join dfd."DocumentSubtype" ds on ds."VCode" = t."DocumentSubtype"
 LEFT JOIN LATERAL comdoc."getDocRouteCurrentStatus"(t."VCode", t."TypeName") AS rst ON true 
where  (t."TypeName" = 'EmployeeStatement' and t."CUser" = t."StageUser") or
             t."TypeName" = 'LND' 
;
```

### Все мои документы и действия в системе

```sql
	insert into "#tmp_finresult"(   "VCode", "TypeName", "RDate", "DocumentNumber","DocumentSubtype","routeId", "attr", "Operation")
	select   t."VCode", t."TypeName", t."RDate", t."DocumentNumber",t."DocumentSubtype",t."routeId", 
(case when not exists (select 1 from comdoc."Route" AS r where r."DocCode" = t."VCode" AND r."DocType" = t."TypeName") 
	                         then 'Маршрут не создан'
							 when t."RouteStatus" = 2 then 'Идет согласование. Текущие участники: ' || rst."CurrentDocflowUser" 
							 when t."RouteStatus" = 3 then 'Согласование завершено'
							 when  exists (select 1 from comdoc."Route" AS r where r."DocCode" = t."VCode" AND r."DocType" = t."TypeName" and r."RouteStatus" = 4)
								and not exists (select 1 from comdoc."Route" AS r where r."DocCode" = t."VCode" AND r."DocType" = t."TypeName" and r."RouteStatus" in(2,3)) then 'Маршрут согласования отменен'
	                        end::text ) ||' '||
 (select string_agg(dca."Name" || ':' || (case 
				when coalesce(dca."AttributeType",'')  = 'string' and  coalesce(atr."Value",'') <> '' then atr."Value"
				when coalesce(dca."AttributeType",'')  = 'string' and coalesce(atr."Value",'') = '' then ' '
				
				when coalesce(dca."AttributeType",'')  = 'bigint' and atr."BigIntValue" is not null then cast(atr."BigIntValue" as varchar(255))
				when coalesce(dca."AttributeType",'')  = 'bigint' and atr."BigIntValue" is null then ' '
				
				when coalesce(dca."AttributeType",'')  = 'string' and atr."BigIntValue" is not null then cast(atr."BigIntValue" as varchar(255))
				when coalesce(dca."AttributeType",'')  = 'string' and atr."BigIntValue" is null then ' '

				when coalesce(dca."AttributeType",'') = 'Base.Unispr' and atr."BigIntValue" is null and coalesce(atr."Value",'') = '' then ' '
				when coalesce(dca."AttributeType",'') = 'Base.Unispr' and atr."BigIntValue" is not null and coalesce(atr."Value",'') <> '' then coalesce(atr."Value",' ')

				when coalesce(dca."AttributeType",'') = 'Base.Post' and atr."BigIntValue" is null and coalesce(atr."Value",'') = '' then ' '
				when coalesce(dca."AttributeType",'') = 'Base.Post' and atr."BigIntValue" is not null and coalesce(atr."Value",'') <> '' then coalesce(atr."Value",' ')

				when coalesce(dca."AttributeType",'') = 'Base.RP_Worker' and atr."BigIntValue" is null and coalesce(atr."Value",'') = '' then ' '
				when coalesce(dca."AttributeType",'') = 'Base.RP_Worker' and atr."BigIntValue" is not null and coalesce(atr."Value",'') <> '' then coalesce(atr."Value",' ')

				when coalesce(dca."AttributeType",'') = 'Base.Contract' and atr."BigIntValue" is null and coalesce(atr."Value",'') = '' then ' '
				when coalesce(dca."AttributeType",'') = 'Base.Contract' and atr."BigIntValue" is not null and coalesce(atr."Value",'') <> '' then coalesce(atr."Value",' ')

				when coalesce(dca."AttributeType",'') = 'Base.Contractor' and atr."BigIntValue" is null and coalesce(atr."Value",'') = '' then ' '
				when coalesce(dca."AttributeType",'') = 'Base.Contractor' and atr."BigIntValue" is not null and coalesce(atr."Value",'') <> '' then coalesce(atr."Value",' ')

				when coalesce(dca."AttributeType",'') = 'Base.Department' and atr."BigIntValue" is null and coalesce(atr."Value",'') = '' then ' '
				when coalesce(dca."AttributeType",'') = 'Base.Department' and atr."BigIntValue" is not null and coalesce(atr."Value",'') <> '' then coalesce(atr."Value",' ')

				when coalesce(dca."AttributeType",'') = 'money' and atr."MoneyValue"  is not null then cast(atr."MoneyValue" as varchar(255))
				when coalesce(dca."AttributeType",'') = 'money' and atr."MoneyValue"  is  null then ' '

				when coalesce(dca."AttributeType",'') = 'Date' and atr."DateValue"  is not null then to_char(atr."DateValue", 'DD.MM.YYYY')
				when coalesce(dca."AttributeType",'') = 'Date' and atr."DateValue"  is null then ' '

        		when coalesce(dca."AttributeType",'') = 'DateTime' and atr."DateTimeValue"  is not null then to_char(atr."DateValue", 'DD.MM.YYYY')
				when coalesce(dca."AttributeType",'') = 'DateTime' and atr."DateTimeValue"  is null then ' '
			
				when coalesce(dca."AttributeType",'')  = 'double' and atr."DoubleValue"  is not null then cast(atr."DoubleValue" as varchar(255))
				when coalesce(dca."AttributeType",'')  = 'double' and atr."DoubleValue"  is null then ' '

				when coalesce(dca."AttributeType",'')  = 'ServiceWord' and coalesce(atr."Value",'') <> '' then coalesce(atr."Value",' ') 
				when coalesce(dca."AttributeType",'')  = 'ServiceWord' and coalesce(atr."Value",'') = '' then ' '

       	 		when coalesce(dca."AttributeType",'')  = 'bool' and coalesce("BigIntValue"::integer,0) = 0 then substring(coalesce("Value",'|'),	position('|' in coalesce("Value",'|'))+1,char_length(coalesce("Value",'|')))
				when coalesce(dca."AttributeType",'')  = 'bool' and coalesce("BigIntValue"::integer,0) = 1 then substring(coalesce("Value",'|'),0,	position('|' in coalesce("Value",'|')))
								
			end), '; ') AS "x"
				    from   dfd."DocumentAdditionalAttribute" atr 
          			    join dfd."DocumentCategoryAttributeType" dca on atr."CategoryAttributeType" = dca."VCode"
				    where  t."VCode" = atr."PCode" ) ,
        (case when t."TypeName" = 'LND' then 'Поступил ЛНА на ознакомление'
           when t."TypeName" = 'DocumentForSigning' then 'Поступил из 1С документ на подписание'
          when t."TypeName" = 'EmployeeStatement' then 'Создано ' || ds."Name" ||' и отправлено на согласование'
          else 'Поступил документ на подписание'
        end)
	  from "#tmp_preresult" t
  left join dfd."DocumentSubtype" ds on ds."VCode" = t."DocumentSubtype"
 LEFT JOIN LATERAL comdoc."getDocRouteCurrentStatus"(t."VCode", t."TypeName") AS rst ON true ;
```

## Расчетные листки

```sql
	insert into "#tmp_finresult"(   "VCode", "TypeName", "RDate", "DocumentNumber","DocumentSubtype","routeId", "attr", "Operation")
	select  t."VCode", t."TypeName", t."RDate", t."DocumentNumber",t."DocumentSubtype",t."routeId",

(case when not exists (select 1 from comdoc."Route" AS r where r."DocCode" = t."VCode" AND r."DocType" = t."TypeName") 
	                         then 'Маршрут не создан'
							 when t."RouteStatus" = 2 then 'Идет согласование. Текущие участники: ' || rst."CurrentDocflowUser" 
							 when t."RouteStatus" = 3 then 'Согласование завершено'
							 when  exists (select 1 from comdoc."Route" AS r where r."DocCode" = t."VCode" AND r."DocType" = t."TypeName" and r."RouteStatus" = 4)
								and not exists (select 1 from comdoc."Route" AS r where r."DocCode" = t."VCode" AND r."DocType" = t."TypeName" and r."RouteStatus" in(2,3)) then 'Маршрут согласования отменен'
	                        end::text ) ||' '||
 (select string_agg(dca."Name" || ':' || (case 
				when coalesce(dca."AttributeType",'')  = 'string' and  coalesce(atr."Value",'') <> '' then atr."Value"
				when coalesce(dca."AttributeType",'')  = 'string' and coalesce(atr."Value",'') = '' then ' '
				
				when coalesce(dca."AttributeType",'')  = 'bigint' and atr."BigIntValue" is not null then cast(atr."BigIntValue" as varchar(255))
				when coalesce(dca."AttributeType",'')  = 'bigint' and atr."BigIntValue" is null then ' '
				
				when coalesce(dca."AttributeType",'')  = 'string' and atr."BigIntValue" is not null then cast(atr."BigIntValue" as varchar(255))
				when coalesce(dca."AttributeType",'')  = 'string' and atr."BigIntValue" is null then ' '

				when coalesce(dca."AttributeType",'') = 'Base.Unispr' and atr."BigIntValue" is null and coalesce(atr."Value",'') = '' then ' '
				when coalesce(dca."AttributeType",'') = 'Base.Unispr' and atr."BigIntValue" is not null and coalesce(atr."Value",'') <> '' then coalesce(atr."Value",' ')

				when coalesce(dca."AttributeType",'') = 'Base.Post' and atr."BigIntValue" is null and coalesce(atr."Value",'') = '' then ' '
				when coalesce(dca."AttributeType",'') = 'Base.Post' and atr."BigIntValue" is not null and coalesce(atr."Value",'') <> '' then coalesce(atr."Value",' ')

				when coalesce(dca."AttributeType",'') = 'Base.RP_Worker' and atr."BigIntValue" is null and coalesce(atr."Value",'') = '' then ' '
				when coalesce(dca."AttributeType",'') = 'Base.RP_Worker' and atr."BigIntValue" is not null and coalesce(atr."Value",'') <> '' then coalesce(atr."Value",' ')

				when coalesce(dca."AttributeType",'') = 'Base.Contract' and atr."BigIntValue" is null and coalesce(atr."Value",'') = '' then ' '
				when coalesce(dca."AttributeType",'') = 'Base.Contract' and atr."BigIntValue" is not null and coalesce(atr."Value",'') <> '' then coalesce(atr."Value",' ')

				when coalesce(dca."AttributeType",'') = 'Base.Contractor' and atr."BigIntValue" is null and coalesce(atr."Value",'') = '' then ' '
				when coalesce(dca."AttributeType",'') = 'Base.Contractor' and atr."BigIntValue" is not null and coalesce(atr."Value",'') <> '' then coalesce(atr."Value",' ')

				when coalesce(dca."AttributeType",'') = 'Base.Department' and atr."BigIntValue" is null and coalesce(atr."Value",'') = '' then ' '
				when coalesce(dca."AttributeType",'') = 'Base.Department' and atr."BigIntValue" is not null and coalesce(atr."Value",'') <> '' then coalesce(atr."Value",' ')

				when coalesce(dca."AttributeType",'') = 'money' and atr."MoneyValue"  is not null then cast(atr."MoneyValue" as varchar(255))
				when coalesce(dca."AttributeType",'') = 'money' and atr."MoneyValue"  is  null then ' '

				when coalesce(dca."AttributeType",'') = 'Date' and atr."DateValue"  is not null then to_char(atr."DateValue", 'DD.MM.YYYY')
				when coalesce(dca."AttributeType",'') = 'Date' and atr."DateValue"  is null then ' '

        		when coalesce(dca."AttributeType",'') = 'DateTime' and atr."DateTimeValue"  is not null then to_char(atr."DateValue", 'DD.MM.YYYY')
				when coalesce(dca."AttributeType",'') = 'DateTime' and atr."DateTimeValue"  is null then ' '
			
				when coalesce(dca."AttributeType",'')  = 'double' and atr."DoubleValue"  is not null then cast(atr."DoubleValue" as varchar(255))
				when coalesce(dca."AttributeType",'')  = 'double' and atr."DoubleValue"  is null then ' '

				when coalesce(dca."AttributeType",'')  = 'ServiceWord' and coalesce(atr."Value",'') <> '' then coalesce(atr."Value",' ') 
				when coalesce(dca."AttributeType",'')  = 'ServiceWord' and coalesce(atr."Value",'') = '' then ' '

       	 		when coalesce(dca."AttributeType",'')  = 'bool' and coalesce("BigIntValue"::integer,0) = 0 then substring(coalesce("Value",'|'),	position('|' in coalesce("Value",'|'))+1,char_length(coalesce("Value",'|')))
				when coalesce(dca."AttributeType",'')  = 'bool' and coalesce("BigIntValue"::integer,0) = 1 then substring(coalesce("Value",'|'),0,	position('|' in coalesce("Value",'|')))
								
			end), '; ') AS "x"
				    from   dfd."DocumentAdditionalAttribute" atr 
          			    join dfd."DocumentCategoryAttributeType" dca on atr."CategoryAttributeType" = dca."VCode"
				    where  t."VCode" = atr."PCode" ) ,

          ('Расчетный лист')
	  from "#tmp_preresult" t
          LEFT JOIN LATERAL comdoc."getDocRouteCurrentStatus"(t."VCode", t."TypeName") AS rst ON true 
          left join dfd."DocumentSubtype" ds on ds."VCode" = t."DocumentSubtype"
	  where ds."InternalName" = 'PaySlip';
``` -->