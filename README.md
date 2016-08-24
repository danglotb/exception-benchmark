# BikiniRepair-benchmark

The BikiniRepair benchmark contains 2 bugs from 2 open-source e-commerce application.

* [mayocat-shop](https://github.com/mayocat/mayocat-shop)
* [Broadleaf Commerce](https://github.com/BroadleafCommerce/BroadleafCommerce)


| Project                    | Bug ID                | Commit ID  |
|----------------------------|-----------------------|------------|
|mayocat-shop                |Mayocat-231            |fb28b82     |
|Broadleaf Commerce          |BroadleafCommerce-1282 |686027c     |















[artifact:mvn] java.lang.NullPointerException
[artifact:mvn] 	at org.broadleafcommerce.openadmin.web.service.FormBuilderServiceImpl.populateEntityForm(FormBuilderServiceImpl.java:718)
[artifact:mvn] 	at org.broadleafcommerce.openadmin.web.controller.entity.AdminBasicEntityController.addEntity(AdminBasicEntityController.java:315)
[artifact:mvn] 	at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
[artifact:mvn] 	at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
[artifact:mvn] 	at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
[artifact:mvn] 	at java.lang.reflect.Method.invoke(Method.java:498)
[artifact:mvn] 	at org.springframework.web.method.support.InvocableHandlerMethod.doInvoke(InvocableHandlerMethod.java:221)
[artifact:mvn] 	at org.springframework.web.method.support.InvocableHandlerMethod.invokeForRequest(InvocableHandlerMethod.java:137)
[artifact:mvn] 	at org.springframework.web.servlet.mvc.method.annotation.ServletInvocableHandlerMethod.invokeAndHandle(ServletInvocableHandlerMethod.java:110)
[artifact:mvn] 	at org.springframework.web.servlet.mvc.method.annotation.RequestMappingHandlerAdapter.invokeHandleMethod(RequestMappingHandlerAdapter.java:776)
[artifact:mvn] 	at org.springframework.web.servlet.mvc.method.annotation.RequestMappingHandlerAdapter.handleInternal(RequestMappingHandlerAdapter.java:705)
[artifact:mvn] 	at org.springframework.web.servlet.mvc.method.AbstractHandlerMethodAdapter.handle(AbstractHandlerMethodAdapter.java:85)
[artifact:mvn] 	at org.springframework.web.servlet.DispatcherServlet.doDispatch(DispatcherServlet.java:959)
[artifact:mvn] 	at org.springframework.web.servlet.DispatcherServlet.doService(DispatcherServlet.java:893)
[artifact:mvn] 	at org.springframework.web.servlet.FrameworkServlet.processRequest(FrameworkServlet.java:966)
[artifact:mvn] 	at org.springframework.web.servlet.FrameworkServlet.doPost(FrameworkServlet.java:868)
[artifact:mvn] 	at javax.servlet.http.HttpServlet.service(HttpServlet.java:647)
[artifact:mvn] 	at org.springframework.web.servlet.FrameworkServlet.service(FrameworkServlet.java:842)
[artifact:mvn] 	at javax.servlet.http.HttpServlet.service(HttpServlet.java:728)
[artifact:mvn] 	at org.apache.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:305)
[artifact:mvn] 	at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:210)
[artifact:mvn] 	at org.springframework.security.web.FilterChainProxy$VirtualFilterChain.doFilter(FilterChainProxy.java:330)
[artifact:mvn] 	at org.springframework.security.web.FilterChainProxy$VirtualFilterChain.doFilter(FilterChainProxy.java:330)
[artifact:mvn] 	at org.broadleafcommerce.openadmin.web.compatibility.JSCompatibilityRequestFilter.doFilterInternal(JSCompatibilityRequestFilter.java:40)
[artifact:mvn] 	at org.springframework.web.filter.OncePerRequestFilter.doFilter(OncePerRequestFilter.java:107)
[artifact:mvn] 	at org.springframework.security.web.FilterChainProxy$VirtualFilterChain.doFilter(FilterChainProxy.java:342)
[artifact:mvn] 	at org.broadleafcommerce.common.web.util.PrecompressedArtifactFilter.doFilter(PrecompressedArtifactFilter.java:89)
[artifact:mvn] 	at org.springframework.security.web.FilterChainProxy$VirtualFilterChain.doFilter(FilterChainProxy.java:342)
[artifact:mvn] 	at org.springframework.web.filter.HiddenHttpMethodFilter.doFilterInternal(HiddenHttpMethodFilter.java:77)
[artifact:mvn] 	at org.springframework.web.filter.OncePerRequestFilter.doFilter(OncePerRequestFilter.java:107)
[artifact:mvn] 	at org.springframework.security.web.FilterChainProxy$VirtualFilterChain.doFilter(FilterChainProxy.java:342)
[artifact:mvn] 	at org.broadleafcommerce.openadmin.web.filter.BroadleafAdminRequestFilter$1.execute(BroadleafAdminRequestFilter.java:73)
[artifact:mvn] 	at org.broadleafcommerce.openadmin.web.filter.BroadleafAdminRequestFilter$1.execute(BroadleafAdminRequestFilter.java:68)
[artifact:mvn] 	at org.broadleafcommerce.openadmin.server.service.persistence.PersistenceThreadManager.operation(PersistenceThreadManager.java:33)
[artifact:mvn] 	at org.broadleafcommerce.openadmin.web.filter.BroadleafAdminRequestFilter.doFilterInternal(BroadleafAdminRequestFilter.java:68)
[artifact:mvn] 	at org.springframework.web.filter.OncePerRequestFilter.doFilter(OncePerRequestFilter.java:107)
[artifact:mvn] 	at org.springframework.security.web.FilterChainProxy$VirtualFilterChain.doFilter(FilterChainProxy.java:342)
[artifact:mvn] 	at org.springframework.web.servlet.resource.ResourceUrlEncodingFilter.doFilterInternal(ResourceUrlEncodingFilter.java:51)
[artifact:mvn] 	at org.springframework.web.filter.OncePerRequestFilter.doFilter(OncePerRequestFilter.java:107)
[artifact:mvn] 	at org.springframework.security.web.FilterChainProxy$VirtualFilterChain.doFilter(FilterChainProxy.java:342)
[artifact:mvn] 	at org.springframework.security.web.FilterChainProxy.doFilterInternal(FilterChainProxy.java:192)
[artifact:mvn] 	at org.springframework.security.web.FilterChainProxy.doFilter(FilterChainProxy.java:166)
[artifact:mvn] 	at org.springframework.security.web.FilterChainProxy$VirtualFilterChain.doFilter(FilterChainProxy.java:342)
[artifact:mvn] 	at org.springframework.security.web.access.intercept.FilterSecurityInterceptor.invoke(FilterSecurityInterceptor.java:108)
[artifact:mvn] 	at org.springframework.security.web.access.intercept.FilterSecurityInterceptor.doFilter(FilterSecurityInterceptor.java:84)
[artifact:mvn] 	at org.springframework.security.web.FilterChainProxy$VirtualFilterChain.doFilter(FilterChainProxy.java:342)
[artifact:mvn] 	at org.springframework.security.web.access.intercept.FilterSecurityInterceptor.invoke(FilterSecurityInterceptor.java:118)
[artifact:mvn] 	at org.springframework.security.web.access.intercept.FilterSecurityInterceptor.doFilter(FilterSecurityInterceptor.java:84)
[artifact:mvn] 	at org.springframework.security.web.FilterChainProxy$VirtualFilterChain.doFilter(FilterChainProxy.java:342)
[artifact:mvn] 	at org.springframework.security.web.access.ExceptionTranslationFilter.doFilter(ExceptionTranslationFilter.java:113)
[artifact:mvn] 	at org.springframework.security.web.FilterChainProxy$VirtualFilterChain.doFilter(FilterChainProxy.java:342)
[artifact:mvn] 	at org.springframework.security.web.session.SessionManagementFilter.doFilter(SessionManagementFilter.java:103)
[artifact:mvn] 	at org.springframework.security.web.FilterChainProxy$VirtualFilterChain.doFilter(FilterChainProxy.java:342)
[artifact:mvn] 	at org.springframework.security.web.authentication.AnonymousAuthenticationFilter.doFilter(AnonymousAuthenticationFilter.java:113)
[artifact:mvn] 	at org.springframework.security.web.FilterChainProxy$VirtualFilterChain.doFilter(FilterChainProxy.java:342)
[artifact:mvn] 	at org.springframework.security.web.servletapi.SecurityContextHolderAwareRequestFilter.doFilter(SecurityContextHolderAwareRequestFilter.java:154)
[artifact:mvn] 	at org.springframework.security.web.FilterChainProxy$VirtualFilterChain.doFilter(FilterChainProxy.java:342)
[artifact:mvn] 	at org.springframework.security.web.savedrequest.RequestCacheAwareFilter.doFilter(RequestCacheAwareFilter.java:45)
[artifact:mvn] 	at org.springframework.security.web.FilterChainProxy$VirtualFilterChain.doFilter(FilterChainProxy.java:342)
[artifact:mvn] 	at org.springframework.security.web.authentication.ui.DefaultLoginPageGeneratingFilter.doFilter(DefaultLoginPageGeneratingFilter.java:155)
[artifact:mvn] 	at org.springframework.security.web.FilterChainProxy$VirtualFilterChain.doFilter(FilterChainProxy.java:342)
[artifact:mvn] 	at org.springframework.security.web.authentication.AbstractAuthenticationProcessingFilter.doFilter(AbstractAuthenticationProcessingFilter.java:199)
[artifact:mvn] 	at org.springframework.security.web.FilterChainProxy$VirtualFilterChain.doFilter(FilterChainProxy.java:342)
[artifact:mvn] 	at org.broadleafcommerce.common.security.handler.CsrfFilter.doFilter(CsrfFilter.java:85)
[artifact:mvn] 	at org.broadleafcommerce.openadmin.web.filter.AdminCsrfFilter.doFilter(AdminCsrfFilter.java:57)
[artifact:mvn] 	at org.springframework.security.web.FilterChainProxy$VirtualFilterChain.doFilter(FilterChainProxy.java:342)
[artifact:mvn] 	at org.springframework.security.web.authentication.logout.LogoutFilter.doFilter(LogoutFilter.java:110)
[artifact:mvn] 	at org.springframework.security.web.FilterChainProxy$VirtualFilterChain.doFilter(FilterChainProxy.java:342)
[artifact:mvn] 	at org.springframework.security.web.context.request.async.WebAsyncManagerIntegrationFilter.doFilterInternal(WebAsyncManagerIntegrationFilter.java:50)
[artifact:mvn] 	at org.springframework.web.filter.OncePerRequestFilter.doFilter(OncePerRequestFilter.java:107)
[artifact:mvn] 	at org.springframework.security.web.FilterChainProxy$VirtualFilterChain.doFilter(FilterChainProxy.java:342)
[artifact:mvn] 	at org.springframework.security.web.context.SecurityContextPersistenceFilter.doFilter(SecurityContextPersistenceFilter.java:87)
[artifact:mvn] 	at org.springframework.security.web.FilterChainProxy$VirtualFilterChain.doFilter(FilterChainProxy.java:342)
[artifact:mvn] 	at org.springframework.security.web.access.channel.ChannelProcessingFilter.doFilter(ChannelProcessingFilter.java:144)
[artifact:mvn] 	at org.springframework.security.web.FilterChainProxy$VirtualFilterChain.doFilter(FilterChainProxy.java:342)
[artifact:mvn] 	at org.springframework.security.web.FilterChainProxy$VirtualFilterChain.doFilter(FilterChainProxy.java:330)
[artifact:mvn] 	at org.springframework.orm.jpa.support.OpenEntityManagerInViewFilter.doFilterInternal(OpenEntityManagerInViewFilter.java:178)
[artifact:mvn] 	at org.springframework.web.filter.OncePerRequestFilter.doFilter(OncePerRequestFilter.java:107)
[artifact:mvn] 	at org.springframework.security.web.FilterChainProxy$VirtualFilterChain.doFilter(FilterChainProxy.java:342)
[artifact:mvn] 	at org.springframework.security.web.FilterChainProxy.doFilterInternal(FilterChainProxy.java:192)
[artifact:mvn] 	at org.springframework.security.web.FilterChainProxy.doFilter(FilterChainProxy.java:166)
[artifact:mvn] 	at org.springframework.security.web.FilterChainProxy$VirtualFilterChain.doFilter(FilterChainProxy.java:342)
[artifact:mvn] 	at org.springframework.security.web.FilterChainProxy.doFilterInternal(FilterChainProxy.java:192)
[artifact:mvn] 	at org.springframework.security.web.FilterChainProxy.doFilter(FilterChainProxy.java:160)
[artifact:mvn] 	at org.springframework.web.filter.DelegatingFilterProxy.invokeDelegate(DelegatingFilterProxy.java:344)
[artifact:mvn] 	at org.springframework.web.filter.DelegatingFilterProxy.doFilter(DelegatingFilterProxy.java:261)
[artifact:mvn] 	at org.apache.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:243)
[artifact:mvn] 	at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:210)
[artifact:mvn] 	at org.springframework.web.filter.CharacterEncodingFilter.doFilterInternal(CharacterEncodingFilter.java:85)
[artifact:mvn] 	at org.springframework.web.filter.OncePerRequestFilter.doFilter(OncePerRequestFilter.java:107)
[artifact:mvn] 	at org.apache.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:243)
[artifact:mvn] 	at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:210)
[artifact:mvn] 	at org.apache.catalina.core.StandardWrapperValve.invoke(StandardWrapperValve.java:222)
[artifact:mvn] 	at org.apache.catalina.core.StandardContextValve.invoke(StandardContextValve.java:123)
[artifact:mvn] 	at org.apache.catalina.authenticator.AuthenticatorBase.invoke(AuthenticatorBase.java:502)
[artifact:mvn] 	at org.apache.catalina.core.StandardHostValve.invoke(StandardHostValve.java:171)
[artifact:mvn] 	at org.apache.catalina.valves.ErrorReportValve.invoke(ErrorReportValve.java:100)
[artifact:mvn] 	at org.apache.catalina.valves.AccessLogValve.invoke(AccessLogValve.java:953)
[artifact:mvn] 	at org.apache.catalina.core.StandardEngineValve.invoke(StandardEngineValve.java:118)
[artifact:mvn] 	at org.apache.catalina.connector.CoyoteAdapter.service(CoyoteAdapter.java:408)
[artifact:mvn] 	at org.apache.coyote.http11.AbstractHttp11Processor.process(AbstractHttp11Processor.java:1041)
[artifact:mvn] 	at org.apache.coyote.AbstractProtocol$AbstractConnectionHandler.process(AbstractProtocol.java:603)
[artifact:mvn] 	at org.apache.tomcat.util.net.JIoEndpoint$SocketProcessor.run(JIoEndpoint.java:312)
[artifact:mvn] 	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1142)
[artifact:mvn] 	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:617)
[artifact:mvn] 	at java.lang.Thread.run(Thread.java:745)
