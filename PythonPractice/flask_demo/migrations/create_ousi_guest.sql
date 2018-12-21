---------------------------create ousi_guest-------------

-- 创建 ousi_guest 表
create table ousi_guest(
       id number primary key,  
       staff_phone varchar2(11),
       name varchar2(8),
       month varchar2(8),
       balance number
);
-- 创建 seq_ousi_guest 序列
create sequence seq_ousi_guest;

-- 创建 tg_ousi_guest 触发器
create or replace trigger tg_ousi_guest before
  INSERT ON ousi_guest FOR EACH row
DECLARE integrity_error EXCEPTION;
  errno  INTEGER;
  errmsg CHAR(200);
  dummy  INTEGER;
  found  BOOLEAN;
BEGIN
  --  Column id uses sequence seq_ousi_guest
  SELECT seq_ousi_guest.NEXTVAL
  INTO :new.id
  FROM dual;
  --  Errors handling

EXCEPTION
WHEN integrity_error THEN
  raise_application_error(errno, errmsg);
END;
/