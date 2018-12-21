---------------------------create ousi_staff-------------

-- 创建 ousi_staff 表
create table ousi_staff(
       sid number primary key,  
       department varchar2(8),
       name varchar2(8),
       password varchar2(8),
       phone varchar2(11),
       role varchar2(8)
);
-- 创建 seq_ousi_staff 序列
create sequence seq_ousi_staff;

-- 创建 tg_ousi_staff 触发器
create or replace trigger tg_ousi_staff before
  INSERT ON ousi_staff FOR EACH row
DECLARE integrity_error EXCEPTION;
  errno  INTEGER;
  errmsg CHAR(200);
  dummy  INTEGER;
  found  BOOLEAN;
BEGIN
  --  Column sid uses sequence seq_ousi_staff
  SELECT seq_ousi_staff.NEXTVAL
  INTO :new.sid -- 注意 id 的名称
  FROM dual;
  --  Errors handling

EXCEPTION
WHEN integrity_error THEN
  raise_application_error(errno, errmsg);
END;
/