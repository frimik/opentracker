#include <errno.h>
#include "io_internal.h"

int64 io_trywritetimeout(int64 d,const char* buf,int64 len) {
  int64 r=io_trywrite(d,buf,len);
  if (r==-1) {
    tai6464 x;
    io_entry* e=array_get(&io_fds,sizeof(io_entry),d);
    taia_now(&x);
    if (!taia_less(&x,&e->timeout)) {
      errno=ETIMEDOUT;
      r=-2;
    }
  }
  return r;
}
