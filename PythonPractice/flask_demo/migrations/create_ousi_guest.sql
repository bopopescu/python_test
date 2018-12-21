---------------------------create ousi_guest-------------

-- ���� ousi_guest ��
create table ousi_guest(
       id number primary key,  
       staff_phone varchar2(11),
       name varchar2(8),
       month varchar2(8),
       balance number
);
-- ���� seq_ousi_guest ����
create sequence seq_ousi_guest;

-- ���� tg_ousi_guest ������
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