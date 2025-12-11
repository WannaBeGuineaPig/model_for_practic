# Настройка правил поиска для ЖСД

В данной форме настраиваются правила поиска документа для [журнала состояния документов](https://ecm-user-manuals.readthedocs.io/ru/latest/User%20manuals/Анализ%20и%20отчетность/#журнал_состояния_документов).
Чтобы открыть данную форму необходимо в Меню в поисковой строке ввести - Настройка правил поиска для ЖСД.

Для создания нового правила в панели инструментов необходимо нажать "Создать".

Откроется новая форма.

![alt text](media/screen1.png)

При нажатии на кнопку **"Показать подсказки"** в верхней части раскрываются рекомендации по работе с данной формой:

![alt text](media/image-5.png)

## Вкладка "Настройки"

На данной вкладке задаются основные настройки поиска документов.

* **Не используется** - при включенной функции данная настройка не будет отображаться в журнале состояния документов.

![alt text](media/image-7.png)

![Фильтр](media/filtr.png)

* **№ / Пользовательское наименование** - указывается порядковый номер и наименование настройки для отображения в журнале состояния документов.

![alt text](media/image-13.png)

![Наименование](media/polNam2.png)

* **Служебное наименование** - указывается служебное наименование по которому фильтруется реестр документов. Служебное наименование должно быть **уникальным** в системе.

![alt text](media/image-14.png)

* **Показывать доп фильтры** - добавляет в журнал дополнительные фильтры: договор, контрагент, инн

* **Показывать в форме** - указывается служебное наименование формы, в которой необходимо отображать данную настройку, например, в личном кабинете HR. Если поле незаполнено то данная настройка отображается во всех формах.

![alt text](media/image-15.png)

![Форма](media/profile.png)

* **доб. списки рассылки** - добавляет в журнал документы полученные через [список рассылки](https://ecm-user-manuals.readthedocs.io/ru/latest/User%20manuals/%D0%9E%D0%B1%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%BA%D0%B0%20%D0%B4%D0%BE%D0%BA%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D0%BE%D0%B2/#%D0%B8%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D1%8F_%D0%BF%D0%BE_%D1%81%D1%82%D0%B0%D1%82%D1%83%D1%81%D0%B0%D0%BC_%D0%BC%D0%B0%D1%80%D1%88%D1%80%D1%83%D1%82%D0%B0_%D0%B2_%D1%80%D0%B5%D0%B5%D1%81%D1%82%D1%80%D0%B0%D1%85_%D0%B4%D0%BE%D0%BA%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D0%BE%D0%B2);

* **рассчитывать просрочку в документах** - рассчитывает количество дней по нарушением сроков обработки в столбце "Просрочено (дней)"

* **Работа России** - отображает кнопку ["Отправить в РР"](https://ecm-user-manuals.readthedocs.io/ru/latest/User%20manuals/%D0%A0%D0%B0%D0%B1%D0%BE%D1%82%D0%B0%20%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D0%B8/) в журнале.

* **ЛНА** - отображает кнопку "Отправить в ЛК сотрудника".

### Скрыть столбцы

* **Подразделение инициатора** - скрывает колонку "Подразделение инициатора";

* **Плановая дата обработки** - скрывает колонку "Плановая дата обработки";

* **Фактическая дата обработки** - скрывает колонку "Фактическая дата обработки";

* **Задача** - скрывает колонку "Задача";

* **Просрочено** - скрывает колонку "Просрочено";

* **Документ** - скрывает колонку "Документ".

* **Дата поступления** - скрывает колонку "Дата поступления";

* **Участник** - скрывает колонку "Участник";

* **Инициатор** - скрывает колонку "Инициатор";

* **Комментарии** - скрывает колонку "Комментарии";

* **Решение** - скрывает колонку "Решение";

* **Вложения** - скрывает колонку "Вложения";

### Добавить группировку

* **по Родительскому подразделению** - добавляет группировку в журнале по родительскому подразделению;

* **по подразделению** - добавляет группировку в журнале по подразделению;

* **по типу документа** - добавляет групп по типу документа;

## Дополнительные колонки (текстовые)

В данном блоке можно добавить дополнительные колонки для отображения в журнале. Наименование колонок может быть произвольным. Информация в дополнительных колонках отображается в зависимости от указанных в [запросе](#вкладка_запрос) условий.

![alt text](media/image-16.png)

В данном блоке могут быть указаны колонки, значения которых можно вычислить на основании реквизитов документов и их маршрутов. 

## Примеры настроек колонок

В колонке **"Статус общий"** указан статус маршрута. Если он "Текущий", то будет заполнена и колонка "На ком документ" пользователями, у которых не выполнено действие на текущем этапе маршрута. Колонка "Согласовавшие участники", напротив, заполняется теми пользователями, у которых уже выполнены действия по маршруту. Эти колонки как правило не нуждаются в донастройке Журнала состояния документов (ЖСД) или конструкторов. 

Колонка **"Реквизиты документа"** в запросах обычно заполняется стандартным значением t."AnyColumnA", в котором перечисляются номер, дата документа и ФИО его создателя.

Колонки **"Период с", "Период по" и "Кол-во"** заполняются значениями дополнительных атрибутов (реквизитов) с хэштегами '#bdate#', '#edate#', '#kolvo#' соответственно, если документ на конструкторе (Заявления от сотрудника, универсальные документы и т.д.), а также заполняются датами и продолжительностью командировки, указанными в теле документа "СЗ на командировку". 

Если уже есть конструкторы, поля которых хотелось бы сопоставить с этими колонками, то можно либо скорректировать запрос в поле **"Итоговая выборка"**, заменив bd.`"ColumnName" = '#bdate#'` на `bd."ColumnName" = '#another_bdate_name#'` (аналогично с другими доп. атрибутами), либо заменить в конструкторе документов старое служебное наименование на новое, не забывая как про основную вкладку с мемо-полем, так и остальные: Ограничения, Сформировать наименование документа из реквизитов, Настройка интерфейса, Настройка проверок, Настройка вычислений.

В колонке **"Прочее"** перечисляются все остальные доп. атрибуты документа и их значения, т.е. со служебными наименованиями, отличными от #bdate#, #edate#, #kolvo#.

Вычисления для колонок **Сотрудник** и **Таб.номер** немного сложнее. Для СЗ на командировку они берутся из таблицы с командированными сотрудниками в документе.

Для универсальных документов и документов на подписание (ДНП) в первую очередь ищется доп.атрибут типа Работник со служебным наименованием, сформированному по правилу #worker%# – это значит, что могут подобраться `#worker#`, `#worker1#` и т.д., т.к. % означает, что после слова worker может идти любой набор симоволов любой длины (даже нулевой). Если такие доп. атрибуты отсутствуют или не заполнены, проверяется, заполнено ли в документе поле IdWorker, которое может быть заполнено кодом сотрудника при загрузке документа из сторонней системы (базы). Для остальных типов документов по умолчанию ищется значение IdWorker.

В заявлениях, актах аннулирования оно заполняется, для ЛНА, доверенностей и прочих документов оно скорее всего не заполняется. Для них можно либо скорректировать запрос в поле **"Итоговая выборка"**, добавив внутрь coalesce вычисление сотрудника по создателю документа или какое-то другое правило.
<!-- , либо определить правило заполнения `IdWorker` в представлении `comdoc."DocflowExists"` (задаётся в базе). -->

Для вычисления родительского подразделения тоже необходимо определить сотрудника, чьё родительское подразделение (а также Инициатор документа, Подразделение, Должность) будет показано в результирующей таблице ЖСД. 

Для универсальных документов и ДНП в первую очередь ищется доп.атрибут со служебным наименованием `#worker#` (или `#Worker#`). Если такой отсутствует или не заполнен, проверяется, заполнено ли в документе поле `IdWorker`, которое может быть заполнено при загрузке документа из сторонней системы (базы). Во всех остальных случаях как для универсальных документов с ДНП, так и остальных типов, берётся пользователь, создавший документ. Если пользователь не заведён как сотрудник, Родительское подразделение не заполнится.

### Настройка колонок

При нажатии на кнопку "Настройка колонок" открывается всплывающее окно, в котором можно назначить порядок отображения столбцов и/или сделать группировку по указанному столбцу. При нажатии на флажок напротив наименования в столбце "Порядок" автоматически проставляется нумерация по отображению порядка столбцов, и также при нажатии в столбце "Группировка".

![alt text](media/screen2.png)

![alt text](media/image-17.png)

![alt text](media/image-22.png)

После внесения изменений необходимо нажать кнопку "Добавить".

![alt text](media/image-20.png)

Назначенные порядки/группировки будут отображаться в поле "Порядок" и в журнале состояния документов:

![alt text](media/image-21.png)

![alt text](media/image-23.png)

## Вкладка "Запрос"

В данном блоке указывается часть с динамическим запросом, содержащим непосредственно запроса для отображения документов.

Для того чтобы документ был ссылочным (переходил в документ по клику наименования документа) необходимо в запросе добавить `"DocCode", "DocType", "DocForm", "DocName"` и проставить галочку "Документ" на вкладке [настройки](#вкладка-настройки)

В запросе возможно настроить цветовое отображение полей документов в зависимости от условий. Для этого в запросе необходимо указать поле "Colors" и заполнить его одним из  следующих значений: `1 -  colors.gray 2 - colors.orange 3 - colors.yellow 4 - colors.green 5 - colors.blue	6 - colors.indigo 7 -colors.violet`. 

!!! example "Пример:"

	В запросе данное значение указывается в конце запроса: 

	```sql
		where wr."COrg" = 4 order by wr."DateBeg" ) as "AnyColumnO"
		, 2
	``` 
	где цифра 2 цвет


Для того чтобы запрос фильтровался по заданному количеству документов, которое указывается в поле **Кол-во строк/Период (с/по):** необходимо в конце запроса добавить строку `_topcount` 

!!! example "Пример:"
	```sql
	left join "tmp_workers_for_documentStatusJournalProc" w2 on w2."VCode" =  t."IdWorker" _topcount;
	```

Для отправки сообщений необходимо заполнить столбец "EmailRecipient" кодом сотрудника в **tmp_finresult**

!!! example "Пример:"
	```sql
	insert into "tmp_finresult"(..., "EmailRecipient")
	...,
	( SELECT w."VCode"
         FROM ...
	limit 1
     )
	```
<!-- ### Примеры запросов

#### Просроченные документы

В реестре отображаются документы, по которым были нарушены сроки обработки

??? note "Запрос" 

	Основной запрос:

	Итоговая выборка:

	```sql
	insert into "tmp_finresult"( "DocCode"   , "DocType"   , "DocForm"  , "DocTypeName"    , "SettingsId"     
  							   , "orgId" , "DocumentDate" , "DocumentNumber"  , "VirtualCUser"  , "DateOfExecution" 
							   , "DateControl"     , "RouteVCode"  , "RouteStatusId"   , "RouteStatusName"  , "DocName"     
							    , "DocSubject"  	  , "expired" , "StageNumber"  	   , "BeginDate"     , "ActionDate"    
								, "DocumentAction" , "DocumentStatus"  , "FromMessage"      , "eDate", "Department"           
	   							, "StageUser"           , "StageItemStatus"  , "StageStatus"      , "StageItemAction" , "DocumentSubtype"   , "AnyColumnA" , "AnyColumnB" , "AnyColumnC" 	, "AnyColumnD" 	, "AnyColumnE")
	select dd."DocCode"   , dd."DocType"   , dd."DocForm"  , dd."DocTypeName"    , dd."SettingsId"     
  							   , dd."orgId" , dd."DocumentDate" , dd."DocumentNumber"  , dd."VirtualCUser"  , dd."DateOfExecution" 
							   , dd."DateControl"     , dd."RouteVCode"  , dd."RouteStatusId"   , dd."RouteStatusName"  , dd."DocName"     
							    , dd."DocSubject"  	  ,    dd."expired", 
								dd."StageNumber"  	   , dd."BeginDate"     , dd."ActionDate"    
								, dd."DocumentAction" , dd."DocumentStatus"  , dd."FromMessage"      , dd."eDate", dd."Department"
	   							, dd."StageUser"           , dd."StageItemStatus"  , dd."StageStatus"      , dd."StageItemAction", dd."DocumentSubtype", dd."AnyColumnA" , dd."AnyColumnB" , dd."AnyColumnC" 	, dd."AnyColumnD" 	, dd."AnyColumnE" 
			from (
			select t."DocCode"   , t."DocType"   , t."DocForm"  , t."DocTypeName"    , t."SettingsId"     
  							   , t."orgId" , t."DocumentDate" , t."DocumentNumber"  , t."VirtualCUser"  , t."DateOfExecution" 
							   , t."DateControl"     , t."RouteVCode"  , t."RouteStatusId"   , t."RouteStatusName"  , t."DocName"     
							    , t."DocSubject"  	  ,   
					comdoc."dfwcGetDuration"(t."eDate", COALESCE(t."ActionDate", _now), false, t."orgId", null, _dayoff1, _dayoff2, null)  as  "expired", 
				t."StageNumber"  	   , t."BeginDate"     , t."ActionDate"    
								, t."DocumentAction" , t."DocumentStatus"  , t."FromMessage"      , t."eDate", t."Department"
	   							, t."StageUser"           , t."StageItemStatus"  , t."StageStatus"      , t."StageItemAction", t."DocumentSubtype", t."AnyColumnA" , t."AnyColumnB" , t."AnyColumnC" 	, t."AnyColumnD" 	, t."AnyColumnE" 
  			from "tmp_preresult" t
  			where coalesce(t."RouteStatusId",0) = 2  and t."IsMarked" is not true
    		and t."StageItemStatus"= 2
	 		AND (
  			t."DocumentDate" IS NULL OR t."DocumentDate" BETWEEN _bdate AND _edate
			)  ) dd
			where 
			coalesce(dd."expired", 0) <> 0 ;
	```

#### Зависшие документы у инициатора

В реестре отображаются документы, которые были инициированы сотрудником, но не запущены далее по маршруту согласования.

??? note "Запрос" 

	![alt text](media/image-24.png)

	Основной запрос:

	Итоговая выборка:

	```sql
	insert into "tmp_finresult"( "DocCode"   , "DocType"   , "DocForm"  , "DocTypeName"    , "SettingsId"     
  							   , "orgId" , "DocumentDate" , "DocumentNumber"  , "VirtualCUser"  , "DateOfExecution" 
							   , "DateControl"     , "RouteVCode"  , "RouteStatusId"   , "RouteStatusName"  , "DocName"     
							    , "DocSubject"  	  , "expired" , "StageNumber"  	   , "BeginDate"     , "ActionDate"    
								, "DocumentAction" , "DocumentStatus"  , "FromMessage"      , "eDate", "Department"
	   							, "StageUser"           , "StageItemStatus"  , "StageStatus"      , "StageItemAction" , "DocumentSubtype", "AnyColumnA" , "AnyColumnB" , "AnyColumnC" 	, "AnyColumnD" 	, "AnyColumnE")
	select t."DocCode"   , t."DocType"   , t."DocForm"  , t."DocTypeName"    , t."SettingsId"     
  							   , t."orgId" , t."DocumentDate" , t."DocumentNumber"  , t."VirtualCUser"  , t."DateOfExecution" 
							   , t."DateControl"     , t."RouteVCode"  , t."RouteStatusId"   , t."RouteStatusName"  , t."DocName"     
							    , t."DocSubject"  	  , 
									comdoc."dfwcGetDuration"(t."eDate", COALESCE(t."ActionDate", _now), false, t."orgId", 1, _dayoff1, _dayoff2, null) , 
								t."StageNumber"  	   , t."BeginDate"     , t."ActionDate"    
								, t."DocumentAction" , t."DocumentStatus"  , t."FromMessage"      , t."eDate", t."Department"
	   							, t."StageUser"           , t."StageItemStatus"  , t."StageStatus"      , t."StageItemAction", t."DocumentSubtype"	, t."AnyColumnA" , t."AnyColumnB" , t."AnyColumnC" 	, t."AnyColumnD" 	, t."AnyColumnE" 
  	from "tmp_preresult" t
  	where coalesce(t."RouteStatusId",0) in ( 2 ) and t."StageItemStatus"= 2 and t."IsMarked" is not true
  	and t."StageNumber" = 1 AND (
  	t."DocumentDate" IS NULL OR t."DocumentDate" BETWEEN _bdate AND _edate
	) ;
	```

#### Поступят к hr в ближайшее время

В реестре отображаются документы, которые в данный момент находятся на стадии согласования у руководителя сотрудника, и после этого поступят в HR службу.

??? note "Запрос" 

	Основной запрос:

	Итоговая выборка:

	```sql
	insert into "tmp_finresult"( "DocCode"   , "DocType"   , "DocForm"  , "DocTypeName"    , "SettingsId"     
  							   , "orgId" , "DocumentDate" , "DocumentNumber"  , "VirtualCUser"  , "DateOfExecution" 
							   , "DateControl"     , "RouteVCode"  , "RouteStatusId"   , "RouteStatusName"  , "DocName"     
							    , "DocSubject"  	  , "expired" , "StageNumber"  	   , "BeginDate"     , "ActionDate"    
								, "DocumentAction" , "DocumentStatus"  , "FromMessage"      , "eDate", "Department"           
	   							, "StageUser"           , "StageItemStatus"  , "StageStatus"      , "StageItemAction" , "DocumentSubtype"   , "AnyColumnA" , "AnyColumnB" , "AnyColumnC" 	, "AnyColumnD" 	, "AnyColumnE")
	select t."DocCode"   , t."DocType"   , t."DocForm"  , t."DocTypeName"    , t."SettingsId"     
  							   , t."orgId" , t."DocumentDate" , t."DocumentNumber"  , t."VirtualCUser"  , t."DateOfExecution" 
							   , t."DateControl"     , t."RouteVCode"  , t."RouteStatusId"   , t."RouteStatusName"  , t."DocName"     
							    , t."DocSubject"  	  ,   
					comdoc."dfwcGetDuration"(t."eDate", COALESCE(t."ActionDate", _now), false, t."orgId", 1, _dayoff1, _dayoff2, null) , 
				t."StageNumber"  	   , t."BeginDate"     , t."ActionDate"    
								, t."DocumentAction" , t."DocumentStatus"  , t."FromMessage"      , t."eDate", t."Department"
	   							, t."StageUser"           , t."StageItemStatus"  , t."StageStatus"      , t."StageItemAction", t."DocumentSubtype", t."AnyColumnA" , t."AnyColumnB" , t."AnyColumnC" 	, t."AnyColumnD" 	, t."AnyColumnE" 
  		from "tmp_preresult" t
  		where coalesce(t."RouteStatusId",0) = 2  and t."IsMarked" is not true
    	and t."StageItemStatus"= 2
		and exists (select 1 from "tmp_userRole" where "Role" not in ( 'hr_docflow_hr', 'hr_director_hr')
				and coalesce(t."StageUser",'') = coalesce("DocflowUser",'') )
		and exists (select 1 from  comdoc."RouteStage" rs 
				join comdoc."StageItem" si on rs."VCode" = si."PCode"
				where  rs."PCode" = t."RouteVCode" 
				and si."StageItemStatus" = 1
				and rs."IsMarked" is not true
				and si."StageUser" in (select "DocflowUser" from "tmp_userRole" where "Role" = 'hr_docflow_hr' ))
	 AND (
 	 t."DocumentDate" IS NULL OR t."DocumentDate" BETWEEN _bdate AND _edate
		) ;
	```

#### Сейчас в работе у hr

В реестре отображаются документы, которые в данный момент находятся в HR службе в работе

??? note "Запрос"

	![alt text](media/image-25.png)

	Основной запрос:

	Итоговая выборка:

	```sql
	insert into "tmp_finresult"( "DocCode"   , "DocType"   , "DocForm"  , "DocTypeName"    , "SettingsId"     
  							   , "orgId" , "DocumentDate" , "DocumentNumber"  , "VirtualCUser"  , "DateOfExecution" 
							   , "DateControl"     , "RouteVCode"  , "RouteStatusId"   , "RouteStatusName"  , "DocName"     
							    , "DocSubject"  	  , "expired" , "StageNumber"  	   , "BeginDate"     , "ActionDate"    
								, "DocumentAction" , "DocumentStatus"  , "FromMessage"      , "eDate", "Department"
	   							, "StageUser"           , "StageItemStatus"  , "StageStatus"      , "StageItemAction" , "IsMarked", "DocumentSubtype"   , "AnyColumnA" , "AnyColumnB" , "AnyColumnC" 	, "AnyColumnD" 	, "AnyColumnE")
	select t."DocCode"   , t."DocType"   , t."DocForm"  , t."DocTypeName"    , t."SettingsId"     
  							   , t."orgId" , t."DocumentDate" , t."DocumentNumber"  , t."VirtualCUser"  , t."DateOfExecution" 
							   , t."DateControl"     , t."RouteVCode"  , t."RouteStatusId"   , t."RouteStatusName"  , t."DocName"     
							    , t."DocSubject"  	  ,   comdoc."dfwcGetDuration"(
                t."eDate", COALESCE(t."ActionDate", _now), false, t."orgId", 1, _dayoff1, _dayoff2, null
            ) 
			, t."StageNumber"  	   , t."BeginDate"     , t."ActionDate"    
								, t."DocumentAction" , t."DocumentStatus"  , t."FromMessage"      , t."eDate", t."Department"
	   							, t."StageUser"           , t."StageItemStatus"  , t."StageStatus"      , t."StageItemAction", t."IsMarked", t."DocumentSubtype"	, t."AnyColumnA" , t."AnyColumnB" , t."AnyColumnC" 	, t."AnyColumnD" 	, t."AnyColumnE" 
  		from "tmp_preresult" t
   		where  coalesce(t."RouteStatusId",0) = 2 and t."StageItemStatus"= 2
 		and coalesce(t."StageUser",'') in (select coalesce("DocflowUser",'') from "tmp_userRole" where "Role" = 'hr_docflow_hr')
	 AND (
  		t."DocumentDate" IS NULL OR t."DocumentDate" BETWEEN _bdate AND _edate
		) ;
	```

#### Обработано службой HR сегодня

В реестре отображаются документы, которые были обработаны сегодня службой HR сегодня.

??? note "Запрос"

	![alt text](media/image-26.png)

	Основной запрос:

	Итоговая выборка:

	```sql
		insert into "tmp_finresult"( "DocCode"   , "DocType"   , "DocForm"  , "DocTypeName"    , "SettingsId"     
  							   , "orgId" , "DocumentDate" , "DocumentNumber"  , "VirtualCUser"  , "DateOfExecution" 
							   , "DateControl"     , "RouteVCode"  , "RouteStatusId"   , "RouteStatusName"  , "DocName"     
							    , "DocSubject"  	  , "expired" , "StageNumber"  	   , "BeginDate"     , "ActionDate"    
								, "DocumentAction" , "DocumentStatus"  , "FromMessage"      , "eDate", "Department"
	   							, "StageUser"           , "StageItemStatus"  , "StageStatus"      , "StageItemAction", "DocumentSubtype" , "AnyColumnA" , "AnyColumnB" , "AnyColumnC" 	, "AnyColumnD" 	, "AnyColumnE"  )
		select t."DocCode"   , t."DocType"   , t."DocForm"  , t."DocTypeName"    , t."SettingsId"     
  							   , t."orgId" , t."DocumentDate" , t."DocumentNumber"  , t."VirtualCUser"  , t."DateOfExecution" 
							   , t."DateControl"     , t."RouteVCode"  , t."RouteStatusId"   , t."RouteStatusName"  , t."DocName"     
							    , t."DocSubject"  	  , 
									comdoc."dfwcGetDuration"(t."eDate", COALESCE(t."ActionDate", _now), false, t."orgId", 1, _dayoff1, _dayoff2, null) , 
								 t."StageNumber"  	   , t."BeginDate"     , t."ActionDate"    
								, t."DocumentAction" , t."DocumentStatus"  , t."FromMessage"      , t."eDate", t."Department"
	   							, t."StageUser"           , t."StageItemStatus"  , t."StageStatus"      , t."StageItemAction", t."DocumentSubtype", t."AnyColumnA" , t."AnyColumnB" , t."AnyColumnC" 	, t."AnyColumnD" 	, t."AnyColumnE" 
  		from "tmp_preresult" t
  		where coalesce(t."RouteStatusId",0) in ( 2,3 ) and t."StageItemStatus"= 3 and t."IsMarked" is not true
  		and t."DocumentStatus" not in (19,22,23,32,33,51,99)
		and t."ActionDate"::date = now()::date
		and exists (select 1 from "tmp_userRole" where "Role" = 'hr_docflow_hr' and coalesce(t."StageUser",'') = coalesce("DocflowUser",'') ) 
		AND (
  		t."DocumentDate" IS NULL OR t."DocumentDate" BETWEEN _bdate AND _edate
		) ;
	```

#### Все документы

??? note "Запрос" 

	![alt text](media/image-27.png)

	Основной запрос:

	```sql
		do $myQ$
		declare _str text;
		begin
		_str := 'INSERT INTO "tmp_calcWithBaseParams_for_documentStatusJournalProc"(
       "DocCode", "DocType", "DocForm", "DocTypeName", "SettingsId", "orgId", "DocumentDate", "DocumentNumber", 
		"VirtualCUser", "DateOfExecution", "DateControl","DocumentSubtype", "Department",
		"IdWorker", "DocumentCategory"
		)
		SELECT distinct e."VCode" AS "DocCode", s."DocType", s."DocForm", s."DocName" AS "DocTypeName", s."VCode" AS "SettingsId", e."COrg" AS "orgId", e."DocumentDate", e."DocumentNumber"
     	, e."VirtualCUser", e."DateOfExecution", e."DateControl", e."DocumentSubtype", e."Department",
	 	e."IdWorker",  (select u."DocumentCategory" from dfd."UniversalDocument" u where u."VCode" = e."VCode") /*u."DocumentCategory"*/
		FROM comdoc."DocflowExists" AS e
  		JOIN comdoc."DocflowDocumentSettings" AS s ON s."DocType" = e."TypeName"
  		-- left join dfd."UniversalDocument" u on u."VCode" = e."VCode"
		WHERE 1 = 1 '
		|| case when coalesce("orgParam",-1111)=-1111 then '' else ' and e."COrg" = '||_orgid::text  end
		|| case when EXISTS(SELECT 1 FROM "tmp_docTypes_for_documentStatusJournalProc" t) then '
		and EXISTS(
  		SELECT 1 FROM "tmp_docTypes_for_documentStatusJournalProc" AS t WHERE t."DocType" = e."TypeName"
		)'  else '' end
		|| case when exists(select 1 from "tmp_docSubTypes_for_documentStatusJournalProc" ) then '
		AND EXISTS(
  		SELECT 1 FROM "tmp_docSubTypes_for_documentStatusJournalProc" AS t WHERE comdoc.try_cast_bigint(t."DocSubType") = e."DocumentSubtype"
		) ' else '' end||'
 		and coalesce( e."DocumentDate",'''||_bdate||''') between '''||_bdate||''' and '''||_edate||'''
 		and e."TypeName" not in (''ServiceDesk'');' ;
		-- }} Выборка по основным атрибутам документа
		execute _str;
		end;
		$myQ$;	
	```


	Итоговая выборка:

	```sql
		IF NOT comdoc."isTableExists"('tmp_addAtribute_for_documentStatusJournalProc', 'temp') THEN
  		CREATE TEMP  TABLE "tmp_addAtribute_for_documentStatusJournalProc"(
      "PCode" bigint NOT NULL,
	  worker bigint,
	  bdate text,
	  edate text,
	  kolvo text,
	  other text,
	 /* bdate_new1 text,
	  edate_new1 text,
	  kolvo_new1 text,
	  bdate_new2 text,
	  edate_new2 text,
	  kolvo_new2 text,*/
	  TypeName varchar(255)
	  
  		);--  ON COMMIT DROP;
  		end if;
  
   	 IF NOT comdoc."isTableExists"('tmp_workers_for_documentStatusJournalProc', 'temp') THEN
  		CREATE TEMP TABLE "tmp_workers_for_documentStatusJournalProc"(
      "VCode" bigint NOT NULL,
	  "Login" varchar(255),
	  "NumTab" varchar(255),
	  "NameFull" varchar(255)
  		) ;-- ON COMMIT DROP;
  		end if; 
  
 	 insert into "tmp_addAtribute_for_documentStatusJournalProc"
	 select daa1."PCode", max(case when bd."ColumnName" = '#Worker#' then daa1."BigIntValue" end) as Worker, 
	 max(case when bd."ColumnName" = '#bdate#' then to_char(daa1."DateValue", 'DD.MM.YYYY') end) as bdate, 
	 max(case when bd."ColumnName" = '#edate#' then to_char(daa1."DateValue", 'DD.MM.YYYY') end) as edate, 
	 max(case when bd."ColumnName" = '#kolvo#' then daa1."BigIntValue"::text end) as kolvo, 
 	 string_agg(case when bd."ColumnName" not in ('#bdate#', '#edate#', '#kolvo#','#bdate_new1#', '#edate_new1#', '#kolvo_new1#') then bd."Name" || ':' || (case 
				when coalesce(bd."AttributeType",'')  = 'string' and  coalesce(daa1."Value",'') <> '' then daa1."Value"
				when coalesce(bd."AttributeType",'')  = 'string' and coalesce(daa1."Value",'') = '' then ' '
				
				when coalesce(bd."AttributeType",'')  = 'bigint' and daa1."BigIntValue" is not null then cast(daa1."BigIntValue" as varchar(255))
				when coalesce(bd."AttributeType",'')  = 'bigint' and daa1."BigIntValue" is null then ' '
				
				when coalesce(bd."AttributeType",'')  = 'string' and daa1."BigIntValue" is not null then cast(daa1."BigIntValue" as varchar(255))
				when coalesce(bd."AttributeType",'')  = 'string' and daa1."BigIntValue" is null then ' '

				when coalesce(bd."AttributeType",'') = 'Base.Unispr' and daa1."BigIntValue" is null and coalesce(daa1."Value",'') = '' then ' '
				when coalesce(bd."AttributeType",'') = 'Base.Unispr' and daa1."BigIntValue" is not null and coalesce(daa1."Value",'') <> '' then coalesce(daa1."Value",' ')

				when coalesce(bd."AttributeType",'') = 'Base.Post' and daa1."BigIntValue" is null and coalesce(daa1."Value",'') = '' then ' '
				when coalesce(bd."AttributeType",'') = 'Base.Post' and daa1."BigIntValue" is not null and coalesce(daa1."Value",'') <> '' then coalesce(daa1."Value",' ')

				when coalesce(bd."AttributeType",'') = 'Base.RP_Worker' and daa1."BigIntValue" is null and coalesce(daa1."Value",'') = '' then ' '
				when coalesce(bd."AttributeType",'') = 'Base.RP_Worker' and daa1."BigIntValue" is not null and coalesce(daa1."Value",'') <> '' then coalesce(daa1."Value",' ')

				when coalesce(bd."AttributeType",'') = 'Base.Contract' and daa1."BigIntValue" is null and coalesce(daa1."Value",'') = '' then ' '
				when coalesce(bd."AttributeType",'') = 'Base.Contract' and daa1."BigIntValue" is not null and coalesce(daa1."Value",'') <> '' then coalesce(daa1."Value",' ')

				when coalesce(bd."AttributeType",'') = 'Base.Contractor' and daa1."BigIntValue" is null and coalesce(daa1."Value",'') = '' then ' '
				when coalesce(bd."AttributeType",'') = 'Base.Contractor' and daa1."BigIntValue" is not null and coalesce(daa1."Value",'') <> '' then coalesce(daa1."Value",' ')

				when coalesce(bd."AttributeType",'') = 'Base.Department' and daa1."BigIntValue" is null and coalesce(daa1."Value",'') = '' then ' '
				when coalesce(bd."AttributeType",'') = 'Base.Department' and daa1."BigIntValue" is not null and coalesce(daa1."Value",'') <> '' then coalesce(daa1."Value",' ')

				when coalesce(bd."AttributeType",'') = 'money' and daa1."MoneyValue"  is not null then cast(daa1."MoneyValue" as varchar(255))
				when coalesce(bd."AttributeType",'') = 'money' and daa1."MoneyValue"  is  null then ' '

				when coalesce(bd."AttributeType",'') = 'Date' and daa1."DateValue"  is not null then to_char(daa1."DateValue", 'DD.MM.YYYY')
				when coalesce(bd."AttributeType",'') = 'Date' and daa1."DateValue"  is null then ' '

        		when coalesce(bd."AttributeType",'') = 'DateTime' and daa1."DateTimeValue"  is not null then to_char(daa1."DateValue", 'DD.MM.YYYY')
				when coalesce(bd."AttributeType",'') = 'DateTime' and daa1."DateTimeValue"  is null then ' '
			
				when coalesce(bd."AttributeType",'')  = 'double' and daa1."DoubleValue"  is not null then cast(daa1."DoubleValue" as varchar(255))
				when coalesce(bd."AttributeType",'')  = 'double' and daa1."DoubleValue"  is null then ' '

				when coalesce(bd."AttributeType",'')  = 'ServiceWord' and coalesce(daa1."Value",'') <> '' then coalesce(daa1."Value",' ') 
				when coalesce(bd."AttributeType",'')  = 'ServiceWord' and coalesce(daa1."Value",'') = '' then ' '

       	 		when coalesce(bd."AttributeType",'')  = 'bool' and coalesce(daa1."BigIntValue"::integer,0) = 0 then substring(coalesce(daa1."Value",'|'),	position('|' in coalesce(daa1."Value",'|'))+1,char_length(coalesce(daa1."Value",'|')))
				when coalesce(bd."AttributeType",'')  = 'bool' and coalesce(daa1."BigIntValue"::integer,0) = 1 then substring(coalesce(daa1."Value",'|'),0,	position('|' in coalesce(daa1."Value",'|')))
								
			end) end , '; ')   as other,
	 /*max(case when bd."ColumnName" = '#bdate_new1#' then to_char(daa1."DateValue", 'DD.MM.YYYY') end) as bdate_new1, 
	 max(case when bd."ColumnName" = '#edate_new1#' then to_char(daa1."DateValue", 'DD.MM.YYYY') end) as edate_new1, 
	 max(case when bd."ColumnName" = '#kolvo_new1#' then daa1."BigIntValue"::text end) as kolvo_new1,
 	 max(case when bd."ColumnName" = '#bdate_new2#' then to_char(daa1."DateValue", 'DD.MM.YYYY') end) as bdate_new2, 
	 max(case when bd."ColumnName" = '#edate_new2#' then to_char(daa1."DateValue", 'DD.MM.YYYY') end) as edate_new2, 
	 max(case when bd."ColumnName" = '#kolvo_new2#' then daa1."BigIntValue"::text end) as kolvo_new2,*/
	 max(a."DocType") as TypeName 
	 from dfd."DocumentAdditionalAttribute" daa1
	 join dfd."DocumentCategoryAttributeType" bd on daa1."CategoryAttributeType" = bd."VCode"
	 join "tmp_calcWithBaseParams_for_documentStatusJournalProc_distinctVC" a on daa1."PCode" = a."DocCode"
	 where a."DocType" in ('DocumentForSigining','UniversalDocument', 'EmployeeStatement')
	 group by daa1."PCode";

	 insert into "tmp_workers_for_documentStatusJournalProc"
	 select w."VCode", max(pc."Code") as "Login", max(w."NumTab") as "NumTab", max(w."NameFull") as "NameFull"
	 from rp."RP_Worker" w
	 left join rp."RP_PersonContact" AS pc  on pc."Pcode" = w."IdPerson" AND pc."IdTypeContact" = 6
	 left join rp."RP_WorkerMove" mov on mov."IdWorker" = w."VCode"
	 group by w."VCode" ;

	 insert into "tmp_finresult"( "DocCode", "DocType", "DocForm", "DocTypeName", "SettingsId"     
  	 , "orgId", "DocumentDate", "DocumentNumber", "VirtualCUser", "DateOfExecution" 
	 , "DateControl", "RouteVCode", "RouteStatusId", "RouteStatusName", "DocName"     
	 , "DocSubject", "expired", "StageNumber", "BeginDate", "ActionDate"    
	 , "DocumentAction", "DocumentStatus", "FromMessage", "eDate"           
	 , "StageUser", "StageItemStatus", "StageStatus", "StageItemAction", "IsMarked", "DocumentSubtype"
	 , "AnyColumnA", "AnyColumnB", "AnyColumnC", "AnyColumnD", "AnyColumnE"
	 , "AnyColumnF", "AnyColumnG" , "AnyColumnH", "AnyColumnI", "AnyColumnJ"
	 , "AnyColumnK", "AnyColumnL", "AnyColumnM", "AnyColumnN", "EmailRecipient", "AnyColumnO", "Colors")

	 select t."DocCode", t."DocType", t."DocForm", t."DocTypeName", t."SettingsId"     
	 , t."orgId" , t."DocumentDate" , t."DocumentNumber",      
	 (case when    t."DocType"  in ('UniversalDocument','DocumentForSigning') then w."Login" else   t."VirtualCUser"  end)  ,
 	 null/*t."DateOfExecution"*/
	 , t."DateControl", t."RouteVCode", t."RouteStatusId", t."RouteStatusName", t."DocName"     
	 , t."DocSubject", null/* coalesce(t."expired", case when coalesce(t."eDate", t."ActionDate", _now)<COALESCE(t."ActionDate", _now) then comdoc."dfwcGetDuration"(
                t."eDate", COALESCE(t."ActionDate", _now), false, t."orgId", 1, _dayoff1, _dayoff2, null) end) */
	 , null/* t."StageNumber"  */, null/*t."BeginDate" */, null/*t."ActionDate"   */ 
	 , null/* t."DocumentAction"*/ , null/*t."DocumentStatus" */, null /*t."FromMessage" */, null /*t."eDate"*/
	 , null /*t."StageUser"  */, null /*t."StageItemStatus"*/, null/*t."StageStatus"  */, null/*t."StageItemAction"*/, t."IsMarked", t."DocumentSubtype"	
	 , t."AnyColumnA", null as  "AnyColumnB", null as "AnyColumnC", null as "AnyColumnD" ,  t."AnyColumnE" 
	 , addit.bdate  as "AnyColumnF", addit.edate as "AnyColumnG", addit.kolvo as "AnyColumnH", addit.other as "AnyColumnI", null/*sii."Name"*/ as "AnyColumnJ",
	 case when coalesce(t."RouteStatusId",0) = 2 
			and exists (select 1 from comdoc."RouteStage" rs where rs."PCode" = t."RouteVCode" and rs."StageNumber" = 1 and rs."Status" = 2  ) then 'Не запущен'
  		when coalesce(t."RouteStatusId",0) = 2  and t."StageItemStatus"= 2  and t."StageNumber" > 1 
	        and exists (select 1 from  comdoc."RouteStage" rs where  rs."PCode" = t."RouteVCode" and rs."IsMarked" is not true and rs."StageName"  in ( 'Исполнить')
                           and rs."Status"=1) then 'На согласовании / на согл у рук-ля'
        when coalesce(t."RouteStatusId",0) =  3  
            and not exists (select 1 from  comdoc."RouteStage" rs 
				            join comdoc."StageItem" si on rs."VCode" = si."PCode"
				            where  rs."PCode" = t."RouteVCode" and si."DocumentStatus" in (19,23))  then 'Завершен'
        when coalesce(t."RouteStatusId",0) =  3  
			and exists (select 1 from  comdoc."RouteStage" rs 
				        join comdoc."StageItem" si on rs."VCode" = si."PCode"
				        where  rs."PCode" = t."RouteVCode" and si."DocumentStatus" in (19,23)) then 'Отклонен' end as "AnyColumnK"
	 , ( SELECT DISTINCT string_agg(u."Initials"|| '(' || ds."Name"|| ')' , '; ')  AS "x"
        FROM comdoc."RouteStage" as rs
           join  comdoc."StageItem" AS i on i."PCode" = rs."VCode"
           join comdoc."VUserMeta" AS u ON u."VCode" = i."StageUser"
          join comdoc."DocumentStatus" AS ds ON ds."VCode" = i."DocumentStatus"
         WHERE rs."PCode" = t."RouteVCode" AND i."StageItemStatus" = 3 and coalesce(i."DocumentStatus",0) <> 0) as "AnyColumnL"
	 , case when  t."DocType"  in ('UniversalDocument','DocumentForSigning') then w."NumTab" else w2."NumTab" end as "AnyColumnM"
	 , case when  t."DocType"  in ('UniversalDocument','DocumentForSigning') then w."NameFull" else w2."NameFull" end as "AnyColumnN"
	 , (select wr."VCode" from rp."RP_Worker" wr join rp."RP_PersonContact" pc on wr."IdPerson"= pc."Pcode" and pc."IdTypeContact" = 6  and pc."Code" = t."StageUser" where wr."COrg" = 1 order by wr."DateBeg" limit 1) as "EmailRecipient"
	 , (select wr."VCode" from rp."RP_Worker" wr join rp."RP_PersonContact" pc on wr."IdPerson"= pc."Pcode" and pc."IdTypeContact" = 6 and pc."Code" = t."StageUser" where wr."COrg" = 1 order by wr."DateBeg" limit 1) as "AnyColumnO"
	 , 3
     from "tmp_preresult" t 
	 left join "tmp_addAtribute_for_documentStatusJournalProc" addit on addit."PCode" = t."DocCode" --and addit.TypeName = "DocType"
	 left join "tmp_workers_for_documentStatusJournalProc" w on w."VCode" = addit.worker
	 left join "tmp_workers_for_documentStatusJournalProc" w2 on w2."VCode" =  t."IdWorker"
 	 _topcount;
  	 drop table "tmp_addAtribute_for_documentStatusJournalProc";
	 drop table "tmp_workers_for_documentStatusJournalProc";
	```

#### Документы на подписание, просроченные работниками

??? note "Запрос" 

	Основной запрос:

	Итоговая выборка:

	```sql
 		insert into "tmp_finresult"( "DocCode"   , "DocType"   , "DocForm"  , "DocTypeName"    , "SettingsId"     
  							   , "orgId" , "DocumentDate" , "DocumentNumber"  , "VirtualCUser"  , "DateOfExecution" 
							   , "DateControl"     , "RouteVCode"  , "RouteStatusId"   , "RouteStatusName"  , "DocName"     
							    , "DocSubject"  	  , "expired" , "StageNumber"  	   , "BeginDate"     , "ActionDate"    
								, "DocumentAction" , "DocumentStatus"  , "FromMessage"      , "eDate", "Department"           
	   							, "StageUser"           , "StageItemStatus"  , "StageStatus"      , "StageItemAction" , "DocumentSubtype"   ,
 		"AnyColumnA" , "AnyColumnB" , "AnyColumnC" 	, "AnyColumnD" 	, "AnyColumnE" )
 
		select t."DocCode"   , t."DocType"   , t."DocForm"  , t."DocTypeName"    , t."SettingsId"     
  							   , t."orgId" , t."DocumentDate" , t."DocumentNumber"  , t."VirtualCUser"  , t."DateOfExecution" 
							   , t."DateControl"     , t."RouteVCode"  , t."RouteStatusId"   , t."RouteStatusName"  , t."DocName"     
							    , t."DocSubject"  	  ,   
					comdoc."dfwcGetDuration"(t."eDate", COALESCE(t."ActionDate", _now), false, t."orgId", 1, _dayoff1, _dayoff2, null) , 
				t."StageNumber"  	   , t."BeginDate"     , t."ActionDate"    
								, t."DocumentAction" , t."DocumentStatus"  , t."FromMessage"      , t."eDate", t."Department"
	   							, t."StageUser"           , t."StageItemStatus"  , t."StageStatus"      , t."StageItemAction", t."DocumentSubtype",
              t."DocTypeName"  as "AnyColumnA" ,  
               p."Family" || ' '|| p."Name" || ' '|| p."Father" as "AnyColumnB" ,  
              t."DocCode" as "AnyColumnC", t."AnyColumnD" 	, t."AnyColumnE" 
		from "tmp_preresult" t
		inner join comdoc."Route" r on t."RouteVCode" = r."VCode"
		inner join comdoc."RouteStage" rs on r."VCode" = rs."PCode" and t."StageNumber"= rs."StageNumber"
		left join rp."RP_PersonContact" pc on pc."Code" = t."StageUser"  and  pc."IdTypeContact" = 6
		left join rp."RP_Person" p on pc."Pcode" = p."VCode"
		where coalesce(t."RouteStatusId",0) in (2) and t."StageItemStatus"= 2 and t."IsMarked" is not true
   		and rs."StageName" ilike '%работник%'
   		and coalesce(t."ActionDate",t."DocumentDate") BETWEEN  _bdate AND _edate 
  		;
	```

#### Договоры и доп. соглашения

??? note "Запрос"

	![alt text](media/image-29.png)

	Основной запрос:

	```sql
		do $newQ$
	 declare _str text;
	 begin
	 _str := '
	 INSERT INTO "tmp_calcWithBaseParams_for_documentStatusJournalProc"(
        "DocCode", "DocType", "DocForm", "DocTypeName", "SettingsId", "orgId", "DocumentDate", "DocumentNumber", 
    	"VirtualCUser", "Department", "IdWorker"
  		)a
  		SELECT e."VCode" AS "DocCode", s."DocType", s."DocForm", s."DocName" AS "DocTypeName", s."VCode" AS "SettingsId", e."COrg" AS "orgId", e."DateContract", e."VhodNumber"
      , e."CUser", e."CuratorDepartmentSpr", e."Manager"
  		FROM contract."Contract" AS e
    	JOIN comdoc."DocflowDocumentSettings" AS s ON s."DocType" = e."TypeName"
  		WHERE 1 = 1
  		'||case when coalesce("orgParam",-1111)=-1111 then '' else ' and e."COrg" = '||_orgid::text end ||'
   		and EXISTS( SELECT 1 FROM "tmp_docTypes_for_documentStatusJournalProc" AS t WHERE t."DocType" = e."TypeName" ) 
  	 '|| case when _contractor is null then '' else ' and e."Contractor" = '||_contractor::text end 
     || case when _contract is null then '' else ' and e."VCode" = '||_contract::text end
  	 || case when _manager is null then '' else ' and e."Manager" = '||_manager::text end
     || ' and e."DateContract" between '_bdate' and '_edate'
   	 union all
  	 SELECT e."VCode" AS "DocCode", s."DocType", s."DocForm", s."DocName" AS "DocTypeName", s."VCode" AS "SettingsId", e."COrg" AS "orgId", e."DateContract", e."Number"
      , e."CUser", e."CuratorDepartmentSpr", e."Manager"
  	 FROM contract."AdditionalContract" AS e
     JOIN comdoc."DocflowDocumentSettings" AS s ON s."DocType" = e."TypeName"
  	 WHERE 1= 1
     '||case when coalesce("orgParam",-1111)=-1111 then '' else ' and e."COrg" = '||_orgid::text end ||'
     and EXISTS( SELECT 1 FROM "tmp_docTypes_for_documentStatusJournalProc" AS t WHERE t."DocType" = e."TypeName" ) 
	 '|| case when _contractor is null then '' else ' and e."Contractor" = '||_contractor::text end 
   	 || case when _contract is null then '' else ' and e."Contract" = '||_contract::text end 
   	 || case when _addcontract is null then '' else ' and e."VCode" = '||_addcontract::text end 
   	 || case when _manager is null then '' else ' and e."Manager" = '||_manager::text end 
   	 || ' and e."DateContract" between '_bdate' and '_edate';';

	 execute (_str);
	 end;
	 $newQ$;
	``` 

	Итоговая выборка:

	```sql
		do
		$$
    	begin
  	 --CREATE INDEX IF NOT EXISTS "idx_tr1_tmp_CategoryAttributeType" ON "tmp_CategoryAttributeType"("PCode" );
 
	 if not comdoc."isTableExists"('tmp_UserRole','temp') then
			 create temp table "tmp_UserRole" ( 
			 "login" character varying(255), "Role" character varying(255)
			 ) 
 	 --on commit drop 
	 ;
	 end if;

	 insert into "tmp_UserRole" ("login", "Role")
	 select  distinct au."UserName" as login,"Role"
	 FROM lex."UserMeta" au
     JOIN lex."OrganizationUser" ou ON au."Id" = ou."User"
 	 left join lex."OrganizationUserRole" ur on ou."Id" = ur."OrganizationUser"
	 where "Role" in ('bh_purchasing_department', 'bh_legal_department', 'bh_contract_administrator', 'bh_financial_services')
	 or "Role" like '%ddc%'
	 ;

 	 if not comdoc."isTableExists"('tmp_CuserChief','temp') then
			 create temp table "tmp_CuserChief" ( 
			 "VirtualCUser" character varying(255), "chief" character varying(255)
			 ) 
 	 --on commit drop 
	 ;
	 end if;

	 insert into "tmp_CuserChief" ("VirtualCUser","chief")
  	 select "VirtualCUser", chief."chief"
  	 from (select distinct t."DocCode",t."DocType" , t."orgId", t."VirtualCUser"  from  "tmp_preresult" t where t."DocType" in ('Base.Contract','Base.AdditionalContract')) t
  	 left join lateral  comdoc."getProjectTemplateMember"(t."DocCode",t."DocType" , t."orgId", t."VirtualCUser", 'Service.Chief') chief on true
 	 ;
  
	 if not comdoc."isTableExists"('tmp_ExpiredRole','temp') then
			 create temp table "tmp_ExpiredRole" ( 
			 "DocCode" bigint, "Role" character varying(255), "maxexpired" int
			 ) 
  	 --on commit drop 
	 ;
	 end if;

 	 insert into "tmp_ExpiredRole" ("DocCode","Role", "maxexpired")
	 select a."DocCode",   a."Role",  max(a."expired")  as "maxexpired"
 	 from
 	 (
 	 select  t."DocCode", t."StageUser",  -- ur."Role", 	coalesce(ch.ф"chief",'') as "chief",
	 case when coalesce(ch."chief",'') <>'' then 'chief_role' else ur."Role" end as "Role",
	 round(comdoc."dfwcGetDuration"(t."eDate", COALESCE(t."ActionDate", _now::date), false, t."orgId", null, _dayoff1, _dayoff2, null)/60.0/60.0/9, 0)    as  "expired"

 	 from (select distinct "DocCode", t."StageUser", t."eDate", t."ActionDate",t."orgId"  from  "tmp_preresult" t where t."DocType"  in ('Base.Contract','Base.AdditionalContract')) t
 	 left join "tmp_UserRole" ur on t."StageUser"= ur."login"
	 left join "tmp_CuserChief" ch on t."StageUser" = ch."chief"
 
 	 ) a 
 	 where coalesce(a."expired", 0) > 0  
 	 group by a."DocCode",  a."Role";
  	 end;
 	 $$;
	
	 insert into "tmp_finresult"( "DocCode"   , "DocType"   , "DocForm"  , "DocTypeName"    , "SettingsId"     
  							   , "orgId" , "DocumentDate" , "DocumentNumber"  , "VirtualCUser"  , "DateOfExecution" 
							   , "DateControl"     , "RouteVCode"  , "RouteStatusId"   , "RouteStatusName"  , "DocName"     
							    , "DocSubject"  	  , "expired" , "StageNumber"  	   , "BeginDate"     , "ActionDate"    
								, "DocumentAction" , "DocumentStatus"  , "FromMessage"      , "eDate", "Department"
	   							, "StageUser"           , "StageItemStatus"  , "StageStatus"      , "StageItemAction" , "DocumentSubtype"
   	 , "AnyColumnA" , "AnyColumnB" , "AnyColumnC" 	, "AnyColumnD" 	, "AnyColumnE" 
 	 , "AnyColumnF" , "AnyColumnG" , "AnyColumnH" 	, "AnyColumnI" 	, "AnyColumnJ" 
	 , "AnyColumnK" , "AnyColumnL" , "AnyColumnM" 	, "AnyColumnN" 	, "AnyColumnO" 
	 ,  "AnyColumnP", "AnyColumnQ" , "AnyColumnR" , "AnyColumnS" 	, "AnyColumnT" 	
	 , "AnyColumnU" , "AnyColumnV" , "AnyColumnW" , "AnyColumnX" , "AnyColumnY" 
	 , "AnyColumnZ" , "AnyColumnAA" , "AnyColumnAB" , "AnyColumnAC" , "AnyColumnAD" , "AnyColumnAE" , "AnyColumnAF" 
 	 , "AnyColumnAG"  , "AnyColumnAH"  , "AnyColumnAI"  , "AnyColumnAJ" , "AnyColumnAK" , "AnyColumnAL"  , "AnyColumnAM" 
	 , "Colors", "attFilter"
	 )
 	 
	 select distinct t."DocCode"   , t."DocType"   , t."DocForm"  , t."DocTypeName"    , t."SettingsId"     
  	 , t."orgId" , t."DocumentDate" , t."DocumentNumber"  , t."VirtualCUser"  , t."DateOfExecution" 
	 , t."DateControl", t."RouteVCode"  , t."RouteStatusId"   , t."RouteStatusName"  , t."DocName"     
	 , t."DocSubject",   	null::bigint ,  	null::int as  "StageNumber"  	   , null::date as  "BeginDate"     , null::date as "ActionDate"    
	 , null::int as  "DocumentAction" ,null::int as  "DocumentStatus"  , null as"FromMessage"      , null::date as "eDate", t."Department"
	 , null as "StageUser", null::int  as "StageItemStatus"  , null::int  as "StageStatus", null::int  as "StageItemAction", t."DocumentSubtype",
	 "Number" as "AnyColumnA", 
	 "VhodNumber" as "AnyColumnB",
	 to_char("DateContract", 'DD.MM.YYYY' ) as "AnyColumnC",
     to_char("DateBegin", 'DD.MM.YYYY' ) as "AnyColumnD",
	 to_char("DateEnd", 'DD.MM.YYYY' ) as  "AnyColumnE",
	 null as  "AnyColumnF",
	 case when coalesce("IsDocument",false) = true then 'Да' else 'Нет' end as  "AnyColumnG",
	 "StatusOfContract" as  "AnyColumnH", 
	 "Contractor" as  "AnyColumnI", 
	 "VTypeContract" as  "AnyColumnJ",
	 "ContractKind1" as  "AnyColumnK",
	 null as  "AnyColumnL",
	 "SumContract" as  "AnyColumnM",
	 "TypePayment" as  "AnyColumnN",
	 "SubjectOfContract" as  "AnyColumnO",
	 null as  "AnyColumnP", 
	 to_char("DateAutolong", 'DD.MM.YYYY' ) as  "AnyColumnQ",
	 null as  "AnyColumnR", 
	 null as  "AnyColumnS",
	 null as  "AnyColumnT",
	 COALESCE(rst."RouteStatusNm", 'Не запущен')  as  "AnyColumnU"
	 , ( SELECT string_agg(r_info."x", ';') FROM
		( SELECT 'Этап '||s."StageNumber"||' '||du."Initials"||COALESCE(' '||ds."Name", '')||COALESCE(' '||i."FromMessage", '') AS "x"
         FROM comdoc."Route" AS r
           JOIN comdoc."RouteStage" AS s ON s."PCode" = r."VCode"
           JOIN comdoc."StageItem" AS i ON i."PCode" = s."VCode"
           JOIN comdoc."VUserMeta" AS du ON du."VCode" = i."StageUser"
           LEFT JOIN comdoc."DocumentStatus" AS ds ON ds."VCode" = i."DocumentStatus"
         WHERE r."DocCode" = t."DocCode"
           AND r."DocType" = t."DocType"
           AND r."RouteStatus" <> 4
         ORDER BY s."StageNumber" ASC, i."VCode" ASC
       ) as r_info )  as "AnyColumnV",
	 null as "AnyColumnW", --бренд
	 null as "AnyColumnX", --парал импорт
	 null as "AnyColumnY", -- с НДС
	 (select  "maxexpired" from "tmp_ExpiredRole"  er where t."DocCode" = er."DocCode" and "Role"='chief_role')   as "AnyColumnZ",--просрочено рук
	 (select  "maxexpired" from "tmp_ExpiredRole"  er where t."DocCode" = er."DocCode" and "Role"='bh_financial_services')  as "AnyColumnAA",--просрочено фин
	 (select  "maxexpired" from "tmp_ExpiredRole"  er where t."DocCode" = er."DocCode" and "Role"='bh_legal_department')  as "AnyColumnAB",--просрочено прав деп
	 (select  "maxexpired" from "tmp_ExpiredRole"  er where t."DocCode" = er."DocCode" and "Role"='bh_purchasing_department')  as "AnyColumnAC",--просрочено закупки
	 (select  "maxexpired" from "tmp_ExpiredRole"  er where t."DocCode" = er."DocCode" and "Role" like '%ddc%')  as "AnyColumnAD", --просрочено ДДЦ
	 (select  "maxexpired" from "tmp_ExpiredRole"  er where t."DocCode" = er."DocCode" and "Role"='bh_contract_administrator') as "AnyColumnAE", --просрочен админ дог
	 t."DocCode" as "AnyColumnAF" 

	 --надо найти зама
	 , (SELECT DISTINCT string_agg(x."UserName", ',') FROM 
			(select 
			m."LastName" || ' ' || m."FirstName" || ' ' || m. "MiddleName"	as "UserName"  
	 --m."UserName", m1."UserName" as "UserName1"
			from lex."UserMeta" as m
			join lex."OrganizationUser" as ou on m."Id" = ou."User" and coalesce(ou."IsBlocked",false) = false 
			join lex."Replacement" as rep on ou."Id" = rep."Replacer" 
					--AND now() between coalesce(rep."BeginDate",now()) AND coalesce(rep."EndDate",now())
			and  coalesce(rep."BeginDate",now())::date<= "DateEnd"::date and coalesce(rep."EndDate",now())::date>= "DateBegin"::date 
			join lex."OrganizationUser" as ou1 on rep."Replaceable" = ou1."Id" --and coalesce(ou1."IsBlocked",false) = false
			join lex."UserMeta" as m1 on ou1."User" = m1."Id"
			where m1."UserName" = t."VirtualCUser"
			group by m."LastName" || ' ' || m."FirstName" || ' ' || m. "MiddleName"	 
	 -- m."UserName", m1."UserName"
			) as x )  ::character varying(1000) AS  "AnyColumnAG"
	 --надо найти руководителя по штатке 
	 ,
	
 	 (select  um."LastName" || ' ' ||um."FirstName" || ' ' ||um."MiddleName"	as "UserName" 
  	 from comdoc."Department" dep 
     join rp."RP_Worker" w on dep."Manager" = w."VCode"
	 join rp."RP_PersonContact" pers on w."IdPerson" = pers."Pcode" and pers."IdTypeContact" = 6
	 join lex."UserMeta" um on um."UserName" = pers."Code"
	 where dep."VCode" = (select "Department" from comdoc."DocflowExists" where "VCode" = t."DocCode"  and "TypeName" = t."DocType"  limit 1) )
	 AS  "AnyColumnAH"
	 , wi."Dpost" AS  "AnyColumnAI", wi."Duvl" AS  "AnyColumnAJ"
 	 ,  c."PaymentMethod" as "AnyColumnAK"  ,  null as "AnyColumnAL"  , 
	 case when coalesce(c."DateAutolong",c."DateEnd",'20701231')::date between now()::date and now()::date + 30::integer
	 then 'yellow'
	 when coalesce(c."DateAutolong",c."DateEnd",'20701231')<now()::date  
	 then 'violet'
	 end as  "AnyColumnAM" 
		,    case when coalesce(c."DateAutolong",c."DateEnd",'20701231')::date between now()::date and now()::date + 30::integer
	 then 3 
	 when coalesce(c."DateAutolong",c."DateEnd",'20701231')<now()::date  
	 then 7 
	 end
 	 as "Colors"
	 , ' and "OrigPriznak" is true ' as "attFilter"

	 /*цвета 1 -  colors.gray 
	 2 - colors.orange
	 3 - colors.yellow
	 4 - colors.green
	 5 - colors.blue
	 6 - colors.indigo
	 7 -colors.violet*/

  	 from  (select distinct t."DocCode"   , t."DocType"   , t."DocForm"  , t."DocTypeName"    , t."SettingsId"     
  	 , t."orgId" , t."DocumentDate" , t."DocumentNumber"  , t."VirtualCUser"  , t."DateOfExecution" 
	 , t."DateControl", t."RouteVCode"  , t."RouteStatusId"   , t."RouteStatusName"  , t."DocName"     
	 , t."DocSubject", t."Department",  t."DocumentSubtype", t."DocumentCategory"
	 from "tmp_preresult" t 
	 where t."DocType" in ('Base.Contract')
  	 )  t
	 inner join  contract."VContractRegistry" c on t."DocCode" = c."VCode"
   	 LEFT JOIN ( SELECT w."VCode", w."lexLogin", dep."VCode" AS "DepartmentVCode", dep."Name" AS "Department", pos."Name" AS "Position" ,to_char(w."DateBeg",'DD.MM.YYYY') as "Dpost",to_char(w."DateEnd",'DD.MM.YYYY') as "Duvl"
  	 FROM rp."VLookupWorker" AS w
     JOIN rp."RP_WorkerMove" AS m ON m."IdWorker" = w."VCode"
     LEFT JOIN comdoc."Department" AS dep ON dep."VCode" = m."IdDepartment"
     LEFT JOIN rp."RP_Post" AS pos ON pos."VCode" = m."IdPost"
  	 WHERE w."lexLogin" IS NOT NULL
  	 ORDER BY ROW_NUMBER() OVER(
     PARTITION BY w."lexLogin"
     ORDER BY   COALESCE(m."DateEnd", w."DateEnd", '2070-01-01'::date) DESC, m."VCode" DESC
  	 )
  	 FETCH FIRST 1 ROWS WITH TIES ) --as  "workers" 
  	 AS wi ON wi."lexLogin" = t."VirtualCUser" 
 	 LEFT JOIN LATERAL comdoc."getDocRouteCurrentStatus"(t."DocCode", t."DocType") AS rst ON true

 	 --where c."DateContract"  BETWEEN _bdate AND _edate

	 /*union all 
	 select distinct t."DocCode"   , t."DocType"   , t."DocForm"  , t."DocTypeName"    , t."SettingsId"     
  	 , t."orgId" , t."DocumentDate" , t."DocumentNumber"  , t."VirtualCUser"  , t."DateOfExecution" 
	 , t."DateControl", t."RouteVCode"  , t."RouteStatusId"   , t."RouteStatusName"  , t."DocName"     
	 , t."DocSubject",   	null::bigint ,  	null::int as  "StageNumber"  	   , null::date as  "BeginDate"     , null::date as "ActionDate"    
	 , null::int as  "DocumentAction" ,null::int as  "DocumentStatus"  , null as"FromMessage"      , null::date as "eDate", t."Department"
	 , null as "StageUser", null::int  as "StageItemStatus"  , null::int  as "StageStatus", null::int  as "StageItemAction", t."DocumentSubtype",
	 ds."Number" as "AnyColumnA", 
	 c."VhodNumber"as "AnyColumnB",
	 to_char(c."DateContract", 'DD.MM.YYYY' ) as "AnyColumnC",
	 to_char(ds."DateBegin", 'DD.MM.YYYY' ) as "AnyColumnD",
	 to_char(ds."DateEnd", 'DD.MM.YYYY' ) as  "AnyColumnE",
	 to_char(ds."DateSignUp", 'DD.MM.YYYY' ) as  "AnyColumnF",
	 case when coalesce(ds."IsDocument",false) = true then 'Да' else 'Нет' end as  "AnyColumnG",
	 ds."StatusOfContractName" as  "AnyColumnH", 
	 ds."ContractorName" as  "AnyColumnI", 
	 c."VTypeContract" as  "AnyColumnJ",
	 c."ContractKind1" as  "AnyColumnK",
	 c."ContractCategory" as  "AnyColumnL",
	 ds."SumWithVAT" as  "AnyColumnM",
	 c."TypePayment" as  "AnyColumnN",
 	 ds."SubjectOfContract" as  "AnyColumnO",
	 c."Autolong" as  "AnyColumnP", 
	 to_char(c."DateAutolong", 'DD.MM.YYYY' ) as  "AnyColumnQ",
	 c."TypicalForm" as  "AnyColumnR", 
	 c."ContractBasis" as  "AnyColumnS",
	 c."CompanyListName" as  "AnyColumnT",
	 COALESCE(rst."RouteStatusNm", 'Не запущен')  as  "AnyColumnU"
	 , ( SELECT string_agg(r_info."x", ';') FROM
		( SELECT 'Этап '||s."StageNumber"||' '||du."Initials"||COALESCE(' '||ds."Name", '')||COALESCE(' '||i."FromMessage", '') AS "x"
         FROM comdoc."Route" AS r
           JOIN comdoc."RouteStage" AS s ON s."PCode" = r."VCode"
           JOIN comdoc."StageItem" AS i ON i."PCode" = s."VCode"
           JOIN comdoc."VUserMeta" AS du ON du."VCode" = i."StageUser"
           LEFT JOIN comdoc."DocumentStatus" AS ds ON ds."VCode" = i."DocumentStatus"
         WHERE r."DocCode" = t."DocCode"
           AND r."DocType" = t."DocType"
           AND r."RouteStatus" <> 4
         ORDER BY s."StageNumber" ASC, i."VCode" ASC
       ) as r_info )  as "AnyColumnV",
		c."BrendName" as "AnyColumnW", --бренд
		c."ParalelImportName" as "AnyColumnX", --парал импорт
	 case when coalesce(c."WithNDS",false) = true then 'С НДС' else 'Без НДС' end as "AnyColumnY", -- с НДС
	 (select  "maxexpired" from "tmp_ExpiredRole"  er where t."DocCode" = er."DocCode" and "Role"='chief_role')   as "AnyColumnZ",--просрочено рук
	 (select  "maxexpired" from "tmp_ExpiredRole"  er where t."DocCode" = er."DocCode" and "Role"='chief_role')  as "AnyColumnAA",--просрочено фин
	 (select  "maxexpired" from "tmp_ExpiredRole"  er where t."DocCode" = er."DocCode" and "Role"='bh_legal_department')  as "AnyColumnAB",--просрочено прав деп
	 (select  "maxexpired" from "tmp_ExpiredRole"  er where t."DocCode" = er."DocCode" and "Role"='chief_role')  as "AnyColumnAC",--просрочено закупки
	 (select  "maxexpired" from "tmp_ExpiredRole"  er where t."DocCode" = er."DocCode" and "Role"='chief_role')  as "AnyColumnAD", --просрочено ДДЦ
	 (select  "maxexpired" from "tmp_ExpiredRole"  er where t."DocCode" = er."DocCode" and "Role"='bh_contract_administrator') as "AnyColumnAE", --просрочен админ дог
	 t."DocCode" as "AnyColumnAF" 
  	 --надо найти зама
	 , (SELECT DISTINCT string_agg(x."UserName", ',') FROM 
			(select 
			m."LastName" || ' ' || m."FirstName" || ' ' || m. "MiddleName"	as "UserName"  
	 --m."UserName", m1."UserName" as "UserName1"
			from lex."UserMeta" as m
			join lex."OrganizationUser" as ou on m."Id" = ou."User" and coalesce(ou."IsBlocked",false) = false 
			join lex."Replacement" as rep on ou."Id" = rep."Replacer" 
					--AND now() between coalesce(rep."BeginDate",now()) AND coalesce(rep."EndDate",now())
			and  coalesce(rep."BeginDate",now())::date<= c."DateEnd"::date and coalesce(rep."EndDate",now())::date>=  c."DateBegin" 
			join lex."OrganizationUser" as ou1 on rep."Replaceable" = ou1."Id" --and coalesce(ou1."IsBlocked",false) = false
			join lex."UserMeta" as m1 on ou1."User" = m1."Id"
			where m1."UserName" = t."VirtualCUser"
			group by m."LastName" || ' ' || m."FirstName" || ' ' || m. "MiddleName"	 
	 -- m."UserName", m1."UserName"
			) as x )  ::character varying(1000) AS  "AnyColumnAG"
	 --надо найти руководителя по штатке 
		,
	
 	 (select  um."LastName" || ' ' ||um."FirstName" || ' ' ||um."MiddleName"	as "UserName" 
  	 from comdoc."Department" dep 
     join rp."RP_Worker" w on dep."Manager" = w."VCode"
	 join rp."RP_PersonContact" pers on w."IdPerson" = pers."Pcode" and pers."IdTypeContact" = 6
	 join lex."UserMeta" um on um."UserName" = pers."Code"
	 where dep."VCode" = (select "Department" from comdoc."DocflowExists" where "VCode" = t."DocCode"  and "TypeName" = t."DocType"  limit 1) )
	 AS  "AnyColumnAH"
	 , wi."Dpost" AS  "AnyColumnAI", wi."Duvl" AS  "AnyColumnAJ"
  	 ,  c."PaymentMethod" as "AnyColumnAK"  ,  c."SumAddContractWithoutVAT" as "AnyColumnAL"  , 
	 null as  "AnyColumnAM" 
	 ,  null as "Colors"
	 from  (select distinct t."DocCode"   , t."DocType"   , t."DocForm"  , t."DocTypeName"    , t."SettingsId"     
  	 , t."orgId" , t."DocumentDate" , t."DocumentNumber"  , t."VirtualCUser"  , t."DateOfExecution" 
	 , t."DateControl", t."RouteVCode"  , t."RouteStatusId"   , t."RouteStatusName"  , t."DocName"     
	 , t."DocSubject", t."Department",  t."DocumentSubtype", t."DocumentCategory"
 	 from "tmp_preresult" t 
		 where t."DocType" in ('Base.AdditionalContract')
  	 )  t
	 inner join contract."VAdditionalContractRegistry" ds on t."DocCode" =ds."VCode"
	 inner join contract."VContractRegistry" c on ds."Contract" = c."VCode"
   	 LEFT JOIN ( SELECT w."VCode", w."lexLogin", dep."VCode" AS "DepartmentVCode", dep."Name" AS "Department", pos."Name" AS "Position" ,to_char(w."DateBeg",'DD.MM.YYYY') as "Dpost",to_char(w."DateEnd",'DD.MM.YYYY') as "Duvl"
  	 FROM rp."VLookupWorker" AS w
     JOIN rp."RP_WorkerMove" AS m ON m."IdWorker" = w."VCode"
     LEFT JOIN comdoc."Department" AS dep ON dep."VCode" = m."IdDepartment"
     LEFT JOIN rp."RP_Post" AS pos ON pos."VCode" = m."IdPost"
  	 WHERE w."lexLogin" IS NOT NULL
  	 ORDER BY ROW_NUMBER() OVER(
     PARTITION BY w."lexLogin"
     ORDER BY   COALESCE(m."DateEnd", w."DateEnd", '2070-01-01'::date) DESC, m."VCode" DESC
  	 )
  	 FETCH FIRST 1 ROWS WITH TIES ) --as  "workers" 
  	 AS wi ON wi."lexLogin" = t."VirtualCUser" 
 	 LEFT JOIN LATERAL comdoc."getDocRouteCurrentStatus"(t."DocCode", t."DocType") AS rst ON true
	 -- where c."DateContract"  BETWEEN _bdate AND _edate
	 */
	```

#### Документы в работе у подчиненных

??? note "Запрос" 

	Основной запрос:

	Итоговая выборка:

	```sql
 			insert into "tmp_finresult"( "DocCode"   , "DocType"   , "DocForm"  , "DocTypeName"    , "SettingsId"     
  							   , "orgId" , "DocumentDate" , "DocumentNumber"  , "VirtualCUser"  , "DateOfExecution" 
							   , "DateControl"     , "RouteVCode"  , "RouteStatusId"   , "RouteStatusName"  , "DocName"     
							    , "DocSubject"  	  , "expired" , "StageNumber"  	   , "BeginDate"     , "ActionDate"    
							    , "DocumentAction" , "DocumentStatus"  , "FromMessage"      , "eDate"           
	   						    , "StageUser"           , "StageItemStatus"  , "StageStatus"      , "StageItemAction" , "DocumentSubtype"   , 
		"AnyColumnA" ,"AnyColumnB" , "AnyColumnC","AnyColumnD"  , 
		"AnyColumnE" ,
		"AnyColumnF", "AnyColumnG" , "AnyColumnH" 	, "AnyColumnI", "AnyColumnJ","AnyColumnK")
		select t."DocCode"   , t."DocType"   , t."DocForm"  , t."DocTypeName"    , t."SettingsId"     
  							   , t."orgId" , t."DocumentDate" , t."DocumentNumber"  ,     
		case when    t."DocType"  in ('UniversalDocument','DocumentForSigning') then (select  pc."Code"   from dfd."DocumentCategoryAttributeType" bd 
                                                                        join dfd."DocumentAdditionalAttribute" daa1 on t."DocCode" = daa1."PCode" and daa1."CategoryAttributeType" = bd."VCode" and bd."ColumnName" = '#Worker#'
                                                                      join rp."RP_Worker" w on w."VCode" = daa1."BigIntValue"
                                                                      join rp."RP_PersonContact" AS pc ON pc."Pcode" = w."IdPerson" AND pc."IdTypeContact" = 6
                                                                        where  t."DocumentCategory" = bd."PCode" limit 1) 
            else   t."VirtualCUser"  end,

			t."DateOfExecution" 
							   , t."DateControl"     , t."RouteVCode"  , t."RouteStatusId"   , t."RouteStatusName"  , t."DocName"     
							    , t."DocSubject"  	  ,   
					comdoc."dfwcGetDuration"(t."eDate", COALESCE(t."ActionDate", _now), false, t."orgId", 1, _dayoff1, _dayoff2, null) , 
				t."StageNumber"  	   , t."BeginDate"     , t."ActionDate"    
								, t."DocumentAction" , t."DocumentStatus"  , t."FromMessage"      , t."eDate"           
	   							, t."StageUser"        , t."StageItemStatus"  , t."StageStatus"      , t."StageItemAction", t."DocumentSubtype", t."AnyColumnA" ,
			case when t."DocType" in ('DocumentForSigining','UniversalDocument') then (select coalesce(w."ID_RP",'')   from dfd."DocumentCategoryAttributeType" bd 
                                                                        join dfd."DocumentAdditionalAttribute" daa1 on t."DocCode" = daa1."PCode" and daa1."CategoryAttributeType" = bd."VCode" and bd."ColumnName" = '#Worker#'
                                                                      join rp."RP_WorkerMove" w on w."IdWorker" = daa1."BigIntValue"
                                                                        where  t."DocumentCategory" = bd."PCode" limit 1) 
                                            else (select coalesce(m."ID_RP",'')  from rp."RP_WorkerMove" AS m where m."IdWorker" =  t."IdWorker" limit 1)  end as  "AnyColumnB" ,
			case when t."DocType" in ('DocumentForSigining','UniversalDocument') then  (select coalesce(w."RP_Txt",'')   from dfd."DocumentCategoryAttributeType" bd 
                                                                        join dfd."DocumentAdditionalAttribute" daa1 on t."DocCode" = daa1."PCode" and daa1."CategoryAttributeType" = bd."VCode" and bd."ColumnName" = '#Worker#'
                                                                      join rp."RP_WorkerMove" w on w."IdWorker" = daa1."BigIntValue"
                                                                        where  t."DocumentCategory" = bd."PCode" limit 1) else (select coalesce(m."RP_Txt",'')  from rp."RP_WorkerMove" AS m where m."IdWorker" =  t."IdWorker" limit 1) end as "AnyColumnC", 
			case when t."DocType" in ('DocumentForSigining','UniversalDocument') then  (select coalesce(w."ID_ER",'')   from dfd."DocumentCategoryAttributeType" bd 
                                                                        join dfd."DocumentAdditionalAttribute" daa1 on t."DocCode" = daa1."PCode" and daa1."CategoryAttributeType" = bd."VCode" and bd."ColumnName" = '#Worker#'
                                                                      join rp."RP_WorkerMove" w on w."IdWorker" = daa1."BigIntValue"
                                                                        where  t."DocumentCategory" = bd."PCode" limit 1) else (select coalesce(m."ID_ER",'')    from rp."RP_WorkerMove" AS m where m."IdWorker" =  t."IdWorker" limit 1) end as "AnyColumnD"  , 
			t."AnyColumnE",
		(select  to_char(daa1."DateValue", 'DD.MM.YYYY')   from dfd."DocumentCategoryAttributeType" bd 
 		join dfd."DocumentAdditionalAttribute" daa1 on t."DocCode" = daa1."PCode" and daa1."CategoryAttributeType" = bd."VCode" and bd."ColumnName" = '#bdate#' where  t."DocumentCategory" = bd."PCode" limit 1)  as "AnyColumnF" ,
		(select  to_char(daa1."DateValue", 'DD.MM.YYYY')   from dfd."DocumentCategoryAttributeType" bd 
 		join dfd."DocumentAdditionalAttribute" daa1 on t."DocCode" = daa1."PCode" and daa1."CategoryAttributeType" = bd."VCode" and bd."ColumnName" = '#edate#' where  t."DocumentCategory" = bd."PCode" limit 1)   as "AnyColumnG" ,
		(select  daa1."BigIntValue"::text  from dfd."DocumentCategoryAttributeType" bd 
 		join dfd."DocumentAdditionalAttribute" daa1 on t."DocCode" = daa1."PCode" and daa1."CategoryAttributeType" = bd."VCode" and bd."ColumnName" ='#kolvo#' where  t."DocumentCategory" = bd."PCode" limit 1)  as "AnyColumnH",
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
				    where  t."DocCode" = atr."PCode" and dca."ColumnName" not in ('#bdate#', '#edate#', '#kolvo#')) as "AnyColumnI",
		case when  t."DocType"  in ('UniversalDocument','DocumentForSigning')  then  (select  w."NumTab"  from dfd."DocumentCategoryAttributeType" bd 
                                                                        join dfd."DocumentAdditionalAttribute" daa1 on t."DocCode" = daa1."PCode" and daa1."CategoryAttributeType" = bd."VCode" and bd."ColumnName" = '#Worker#'
                                                                      join rp."RP_Worker" w on w."VCode" = daa1."BigIntValue"
                                                                        where  t."DocumentCategory" = bd."PCode" limit 1)
            else (select r."NumTab" from rp."RP_Worker" as r where r."VCode" = t."IdWorker")  end ,
		case when  t."DocType"  in ('UniversalDocument','DocumentForSigning')  then  (select  w."NameFull"  from dfd."DocumentCategoryAttributeType" bd 
                                                                        join dfd."DocumentAdditionalAttribute" daa1 on t."DocCode" = daa1."PCode" and daa1."CategoryAttributeType" = bd."VCode" and bd."ColumnName" = '#Worker#'
                                                                      join rp."RP_Worker" w on w."VCode" = daa1."BigIntValue"
                                                                        where  t."DocumentCategory" = bd."PCode" limit 1)
            else (select r."NameFull" from rp."RP_Worker" as r where r."VCode" = t."IdWorker")  end 
		from "tmp_preresult" t
  		where coalesce(t."RouteStatusId",0) = 2  and t."IsMarked" is not true
    	and t."StageItemStatus"= 2 and 
		exists (select 1 
		from comdoc."getWorkerChiefStructure"(null::bigint,lex."getVirtualLogin"(),1) s
        join rp."RP_Worker" r on s."VCode" = r."VCode"
        join rp."RP_PersonContact" c on r."IdPerson" = c."Pcode" and c."IdTypeContact" = 6 
		where c."Code" = coalesce(t."StageUser",'') )
	 	AND (
  		t."DocumentDate" IS NULL OR t."DocumentDate" BETWEEN _bdate AND _edate
		)    and t."DocType" not in ('ServiceDesk', 'CancellationAct') ;
	
	```

#### Универсальные документы подчиненных

??? note "Запрос" 

	Основной запрос:

	Итоговая выборка:

	```sql
 					insert into "tmp_finresult"( "DocCode"   , "DocType"   , "DocForm"  , "DocTypeName"    , "SettingsId"     
  							   , "orgId" , "DocumentDate" , "DocumentNumber"  , "VirtualCUser"  , "DateOfExecution" 
							   , "DateControl"     , "RouteVCode"  , "RouteStatusId"   , "RouteStatusName"  , "DocName"     
							    , "DocSubject"  	  , "expired" , "StageNumber"  	   , "BeginDate"     , "ActionDate"    
							    , "DocumentAction" , "DocumentStatus"  , "FromMessage"      , "eDate"           
	   						    , "StageUser"           , "StageItemStatus"  , "StageStatus"      , "StageItemAction" , "DocumentSubtype"   , 
		"AnyColumnA" ,"AnyColumnB" , "AnyColumnC","AnyColumnD"  , 
		"AnyColumnE" ,
		"AnyColumnF", "AnyColumnG" , "AnyColumnH" 	, "AnyColumnI", "AnyColumnJ","AnyColumnK")
			select distinct t."DocCode"   , t."DocType"   , t."DocForm"  , t."DocTypeName"    , t."SettingsId"     
									, t."orgId" , t."DocumentDate" , t."DocumentNumber"  ,     
		case when    t."DocType"  in ('UniversalDocument','DocumentForSigning') then (select  pc."Code"   from dfd."DocumentCategoryAttributeType" bd 
                                                                        join dfd."DocumentAdditionalAttribute" daa1 on t."DocCode" = daa1."PCode" and daa1."CategoryAttributeType" = bd."VCode" and bd."ColumnName" = '#Worker#'
                                                                      join rp."RP_Worker" w on w."VCode" = daa1."BigIntValue"
                                                                      join rp."RP_PersonContact" AS pc ON pc."Pcode" = w."IdPerson" AND pc."IdTypeContact" = 6
                                                                        where  t."DocumentCategory" = bd."PCode" limit 1) 
            else   t."VirtualCUser"  end,

		t."DateOfExecution" 
							   , t."DateControl"     , t."RouteVCode"  , t."RouteStatusId"   , t."RouteStatusName"  , t."DocName"     
							    , t."DocSubject"  	  ,   
					comdoc."dfwcGetDuration"(t."eDate", COALESCE(t."ActionDate", _now), false, t."orgId", 1, _dayoff1, _dayoff2, null) , 
				t."StageNumber"  	   , t."BeginDate"     , t."ActionDate"    
								, t."DocumentAction" , t."DocumentStatus"  , t."FromMessage"      , t."eDate"           
	   							, t."StageUser"        , t."StageItemStatus"  , t."StageStatus"      , t."StageItemAction", t."DocumentSubtype", t."AnyColumnA" ,
		case when t."DocType" in ('DocumentForSigining','UniversalDocument') then (select coalesce(w."ID_RP",'')   from dfd."DocumentCategoryAttributeType" bd 
                                                                        join dfd."DocumentAdditionalAttribute" daa1 on t."DocCode" = daa1."PCode" and daa1."CategoryAttributeType" = bd."VCode" and bd."ColumnName" = '#Worker#'
                                                                      join rp."RP_WorkerMove" w on w."IdWorker" = daa1."BigIntValue"
                                                                        where  t."DocumentCategory" = bd."PCode" limit 1) 
                                            else (select coalesce(m."ID_RP",'')  from rp."RP_WorkerMove" AS m where m."IdWorker" =  t."IdWorker" limit 1)  end as  "AnyColumnB" ,
		case when t."DocType" in ('DocumentForSigining','UniversalDocument') then  (select coalesce(w."RP_Txt",'')   from dfd."DocumentCategoryAttributeType" bd 
                                                                        join dfd."DocumentAdditionalAttribute" daa1 on t."DocCode" = daa1."PCode" and daa1."CategoryAttributeType" = bd."VCode" and bd."ColumnName" = '#Worker#'
                                                                      join rp."RP_WorkerMove" w on w."IdWorker" = daa1."BigIntValue"
																				where  t."DocumentCategory" = bd."PCode" limit 1) else (select coalesce(m."RP_Txt",'')  from rp."RP_WorkerMove" AS m where m."IdWorker" =  t."IdWorker" limit 1) end as "AnyColumnC", 
		case when t."DocType" in ('DocumentForSigining','UniversalDocument') then  (select coalesce(w."ID_ER",'')   from dfd."DocumentCategoryAttributeType" bd 
                                                                        join dfd."DocumentAdditionalAttribute" daa1 on t."DocCode" = daa1."PCode" and daa1."CategoryAttributeType" = bd."VCode" and bd."ColumnName" = '#Worker#'
                                                                      join rp."RP_WorkerMove" w on w."IdWorker" = daa1."BigIntValue"
                                                                        where  t."DocumentCategory" = bd."PCode" limit 1) else (select coalesce(m."ID_ER",'')    from rp."RP_WorkerMove" AS m where m."IdWorker" =  t."IdWorker" limit 1) end as "AnyColumnD"  , 
		t."AnyColumnE",
		(select  to_char(daa1."DateValue", 'DD.MM.YYYY')   from dfd."DocumentCategoryAttributeType" bd 
		join dfd."DocumentAdditionalAttribute" daa1 on t."DocCode" = daa1."PCode" and daa1."CategoryAttributeType" = bd."VCode" and bd."ColumnName" = '#bdate#' where  t."DocumentCategory" = bd."PCode" limit 1)  as "AnyColumnF" ,
		(select  to_char(daa1."DateValue", 'DD.MM.YYYY')   from dfd."DocumentCategoryAttributeType" bd 
		join dfd."DocumentAdditionalAttribute" daa1 on t."DocCode" = daa1."PCode" and daa1."CategoryAttributeType" = bd."VCode" and bd."ColumnName" = '#edate#' where  t."DocumentCategory" = bd."PCode" limit 1)   as "AnyColumnG" ,
		(select  daa1."BigIntValue"::text  from dfd."DocumentCategoryAttributeType" bd 
		join dfd."DocumentAdditionalAttribute" daa1 on t."DocCode" = daa1."PCode" and daa1."CategoryAttributeType" = bd."VCode" and bd."ColumnName" ='#kolvo#' where  t."DocumentCategory" = bd."PCode" limit 1)  as "AnyColumnH",
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
				    where  t."DocCode" = atr."PCode" and dca."ColumnName" not in ('#bdate#', '#edate#', '#kolvo#')) as "AnyColumnI",
		case when  t."DocType"  in ('UniversalDocument','DocumentForSigning')  then  (select  w."NumTab"  from dfd."DocumentCategoryAttributeType" bd 
                                                                        join dfd."DocumentAdditionalAttribute" daa1 on t."DocCode" = daa1."PCode" and daa1."CategoryAttributeType" = bd."VCode" and bd."ColumnName" = '#Worker#'
                                                                      join rp."RP_Worker" w on w."VCode" = daa1."BigIntValue"
                                                                        where  t."DocumentCategory" = bd."PCode" limit 1)
            else (select r."NumTab" from rp."RP_Worker" as r where r."VCode" = t."IdWorker")  end ,
		case when  t."DocType"  in ('UniversalDocument','DocumentForSigning')  then  (select  w."NameFull"  from dfd."DocumentCategoryAttributeType" bd 
                                                                        join dfd."DocumentAdditionalAttribute" daa1 on t."DocCode" = daa1."PCode" and daa1."CategoryAttributeType" = bd."VCode" and bd."ColumnName" = '#Worker#'
                                                                      join rp."RP_Worker" w on w."VCode" = daa1."BigIntValue"
                                                                        where  t."DocumentCategory" = bd."PCode" limit 1)
					else (select r."NameFull" from rp."RP_Worker" as r where r."VCode" = t."IdWorker")  end 
		from "tmp_preresult" t
		where t."IsMarked" is not true and 
		exists (select 1 
		from comdoc."getWorkerChiefStructure"(null::bigint,lex."getVirtualLogin"(),1) s
				join rp."RP_Worker" r on s."VCode" = r."VCode"
				join rp."RP_PersonContact" c on r."IdPerson" = c."Pcode" and c."IdTypeContact" = 6 
		where c."Code" = coalesce(t."StageUser",'') )
			AND (
		t."DocumentDate" IS NULL OR t."DocumentDate" BETWEEN _bdate AND _edate
		)    and t."DocType" in ('UniversalDocument') ;
	```

#### Выборка из учетной политики

??? note "Запрос" 

	Основной запрос:

	```sql
		do $newQ$
		declare _str text;
		begin
		end;
		$newQ$;
	```

	Итоговая выборка:

	```sql
 		insert into "tmp_finresult"( "DocCode"   , "DocType"   , "DocForm"  , "AnyColumnA"  , "AnyColumnB"  , "AnyColumnC", "AnyColumnD", "AnyColumnE", "AnyColumnF", "orgId", "AnyColumnG", "AnyColumnH"
 	)

		select p."VCode", 'Base.AccountingPolitics', 'RulesForDocumentStatusJournalForm' , f."Name", m."Determination", m."ValueText", m."ValueConst",  to_char(p."WDate",'DD.MM.YYYY'), p."WUser", p."COrg", 
		to_char(p."BeginDate",'DD.MM.YYYY'), to_char(p."EndDate",'DD.MM.YYYY')
		from acc."AccountingPolitics" p
			join comdoc."SettingOfConstants" m on p."VCode" = m."PCode"
			join comdoc."VFilials" f on p."COrg" = f."VCode"
		where now()::date between coalesce(p."BeginDate",'19700101') and  coalesce(p."EndDate",'20700101')
		;
	``` 

#### Аналитическая форма по расписанию задач

??? note "Запрос"

	![alt text](media/image-28.png)

	Основной запрос:

	```sql
		INSERT INTO "tmp_calcWithBaseParams_for_documentStatusJournalProc"( "DocCode" )
	select null;
	```

	Итоговая выборка:

	```sql
 		insert into "tmp_finresult"( "DocCode"   , "DocType"   , "DocForm"  ,  "DocTypeName", "DocName", "DocumentDate",
							"AnyColumnA"  , "AnyColumnB" , "AnyColumnC" 	, "AnyColumnD" 	, "AnyColumnE", 
                                                         "AnyColumnF", "AnyColumnG", "AnyColumnH", "AnyColumnI", "AnyColumnJ")

		select  dd."Id", 'task'::text, 'taskForm'::text, ('Шедулер' || dd."Name")::text, 'Планировщик задач ' ||dd."Name" , dd."CDate"::date,
					dd."Name" as "AnyColumnA" , dd."Description" as "AnyColumnB" , 
				dd."Minutes" as "AnyColumnC" , dd."Hours" as "AnyColumnD" , dd."Days" as "AnyColumnE" , dd."Months" as "AnyColumnF" , dd."DaysOfTheWeek" as "AnyColumnG" ,dd. "Note" as "AnyColumnH" ,dd. "TypeTask" as "AnyColumnI"
				, sum(comdoc."datediff"('minute',j."TimeStart" , j."TimeEnd"))/ count(j."Id") as "AnyColumnJ"
		from (
		select t."Id", t."Name", t."Description",
				sh."Crontab", 
				max(case when s."VCode" = 1 then s."PartString" else '' end) as "Minutes",
				max(case when s."VCode" = 2 then s."PartString" else '' end) as "Hours",
				max(case when s."VCode" = 3 then s."PartString" else '' end) as "Days",
				max(case when s."VCode" = 4 then s."PartString"  else '' end) as "Months",
				max(case when s."VCode" = 5 then s."PartString"  else '' end) as "DaysOfTheWeek",
				'по гринвичу' as "Note", 'Шедулер' as "TypeTask", t."CDate"
		from lex."Task" t 
			join lex."Schedule" sh on t."Id" = sh."Parent"
			LEFT JOIN LATERAL comdoc."LexStringToListNew"(replace(sh."Crontab",' ','Ё'),'Ё',0) s on true
			join (select 1 as "VCode", 'мин.' as "Name"
			union all
			select 2 as "VCode", 'часы' as "Name"
			union all
			select 3 as "VCode", 'день' as "Name"
			union all
			select 4 as "VCode", 'месяц' as "Name"
			union all
			select 5 as "VCode", 'дни недели' as "Name"
							) d on s."VCode" = d."VCode"
				
			--  inner join lex."StepJournalEntryDetail" s on j."Id" = s."PCode"
			where coalesce(t."Toggle",false) = true
		group by t."Id", t."Name", t."Description", sh."Crontab",  t."CDate"
			)dd
		left  join lex."TaskJournalEntry" j on dd."Id" = j."TaskId" and  j."TimeStart">= now()::date - '1 month'::interval and j."TimeEnd" is not null	
		--where j."TimeStart">= now()::date - '1 month'::interval and j."TimeEnd" is not null
		group by dd."Id", dd."Name", dd."Description", dd."Crontab", "Minutes", "Hours", "Days", "Months", "DaysOfTheWeek", "Note", "TypeTask",  dd."CDate"

		union all
		select t."VCode", 'NotificationLexemaDirectory'::text, 'NotificationLexemaDirectoryForm'::text , '', ( 'Задачи планировщика ' ||t."TaskName") ::text,  t."CDate"::date,
					t."TaskName" as "AnyColumnA" , null::text as "AnyColumnB" , 
				t."Minutes" as "AnyColumnC" , t."Hours" as "AnyColumnD" , t."Days" as "AnyColumnE" , t."Months" as "AnyColumnF" , t."DaysOfTheWeek" as "AnyColumnG" ,'серверное время' as "AnyColumnH" ,'Задачи планировщика'  as "AnyColumnI", 
				null::int as "AnyColumnJ"
		from dfd."NotificationLexemaDirectory" t
		where coalesce(t."Included",false) = true;
	```

#### Логи отправки почты и СМС

Необходимо дополнительно настроить [задачу планировщика](../Функции%20планировщика%20задач/#перенос_логов_отправки_почты_и_смс_в_таблицу_sendlog)

??? note "Запрос"

	![alt text](media/image-30.png)

	Основной запрос:

	```sql
					INSERT INTO "tmp_calcWithBaseParams_for_documentStatusJournalProc"( "DocCode")
			select 1 from dfd."OutgoingEmailLog" where 1 = 1
			limit 1;
			```

			Итоговая выборка:

			```sql
				do $myQ$
		declare _str text;
		begin
		_str := '
		insert into "tmp_finresult"("AnyColumnA", "AnyColumnB", "AnyColumnC", "AnyColumnD", "AnyColumnE", "AnyColumnF", "AnyColumnG", "AnyColumnH", "AnyColumnI", "AnyColumnJ", "AnyColumnK", "AnyColumnL", "AnyColumnM")
		select p."Level", p."type", p."To", p."Subject", p."Body", p."Cc", p."Bcc", p."phones", p."text", p."errorText", 
				to_char(p."CDateLog",''DD.MM.YYYY hh:mi'') as "CDateLog", p."CUserLog", p."CHostLog"
		from comdoc."SendLog" p
		where  coalesce( p."CDateLog"::date,'_bdate'::date) between '_bdate'::date and '_edate'::date
		order by p."CDateLog" desc' 
		_topcount ;
		execute _str;
		end;
		$myQ$;
	``` -->
